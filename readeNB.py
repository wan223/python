import pymysql  # 操作mysql的模块
import openpyxl  # xlsx格式对应的操作模块
import time
import threadpool  # 线程池模块
import math
from datetime import datetime

successList = []  # 储存每个线程成功的数目，用于统计


def readRow(rows):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="test", charset="utf8")
    cur = conn.cursor()  # 获取游标

    num = 0
    for row in rows:

        itemNo = row[0].value if row[0].value != None else 111
        itemName = row[1].value.replace("'", "") if row[1].value != None else ""
        itemName = itemName.replace("\\", "|")
        pym = row[2].value.replace("'", "") if row[2].value != None else ""
        pym = pym.replace("\\", "|")
        itemSize = row[3].value.replace("'", "") if row[3].value != None else ""
        itemSize = itemSize.replace("\\", "|")
        unitNo = row[4].value.replace("'", "") if row[4].value != None else ""
        unitNo = unitNo.replace("\\", "|")
        productArea = row[5].value.replace("'", "") if row[5].value != None else ""
        productArea = productArea.replace("\\", "|")

        args = (itemNo, itemName, pym, itemSize, unitNo, productArea)
        try:
            sql = r'''
				insert into bar_code_dcm1 (itemNo,itemName,pym,itemSize,unitNo,productArea)
				values
				(%s,'%s','%s','%s','%s','%s') 
				''' % args
            # print(sql, "\r\n----------------------------------------------------------")
            cur.execute(sql)
            conn.commit()
            num = num + 1
        except Exception as e:
            print(Exception, e, "SQL：%s " % sql)
        else:
            pass
        finally:
            pass

        if num % 1000 == 0:
            print("---当前线程已导入：", num, " 条   %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    successList.append(num)
    conn.close()


# time.sleep(1)


def excel2Mysql(excelFileName):
    wb = openpyxl.load_workbook(excelFileName)  # 打开excel文件 ；16.5s
    sheetList = wb.get_sheet_names()  # 获取工作簿所有工作表名

    for sheetName in sheetList:  # 遍历，每一个工作簿

        sheetObj = wb.get_sheet_by_name(sheetName)  # 获取工作簿对象
        rows = sheetObj.iter_rows()

        bigList = []  # 每个元素为一行excel表格内容
        poolArgsList = []  # 每个元素为一万行excel表格内容,传递给线程池的集合

        for row in rows:
            if len(row[0].value) != 13:  # 过滤掉不标准的条形码数据（标准数字条形码长度为13）
                continue
            else:
                bigList.append(row)

        cycle = math.ceil(len(bigList) / 10000)
        for index in range(1, cycle + 1):
            thisList = bigList[(index - 1) * 10000:index * 10000]  # list切片
            poolArgsList.append(thisList)

        pools = threadpool.ThreadPool(10)  # 初始化10个线程(不一定全用上，python会自己调度，最好是1w数据对应1个线程)
        print("-*-数据读取，组装完毕-*-*-*开启 %d 个线程-*-*-*- \n\r" % 10)
        tasks = threadpool.makeRequests(readRow, poolArgsList)  # 创建任务（处理函数，可迭代对象），每一个迭代元素即为处理函数的参数
        [pools.putRequest(task) for task in tasks]  # 线程池和任务都有了，将任务放入线程池中，执行
        pools.wait()

    wb.close()


if __name__ == '__main__':
    startTime = datetime.now()
    excelFileName = "C:/Users/wanku/Desktop/1-54w.xlsx"
    print("[  %s  ] [ 开始导入 %s " % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), excelFileName), "文件 ]")
    excel2Mysql(excelFileName)
    endTime = datetime.now()
    print("[  %s  ] %s " % (
    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "[ 导入完毕，总导入：" + str(sum(successList)) + "条 ]"),
          "[ 用时 %d 秒]" % (endTime - startTime).seconds)