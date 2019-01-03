import xlrd
import xlwt
import pymysql


def read(file, sheet_index=0):
    """

    :param file: 文件路径
    :param sheet_index: 读取的工作表索引
    :return: 二维数组
    """
    workbook = xlrd.open_workbook(file)
    # all_sheets_list = workbook.sheet_names()
    # print("本文件中所有的工作表名称:", all_sheets_list)
    # 按索引读取工作表
    sheet = workbook.sheet_by_index(sheet_index)
    print("工作表名称:", sheet.name)
    print("行数:", sheet.nrows)
    print("列数:", sheet.ncols)

    # 按工作表名称读取数据
    # second_sheet = workbook.sheet_by_name("b")
    # print("Second sheet Rows:", second_sheet.nrows)
    # print("Second sheet Cols:", second_sheet.ncols)
    # 获取单元格的数据
    # cell_value = sheet.cell(1, 0).value
    # print("获取第2行第1列的单元格数据:", cell_value)
    data = []
    for i in range(0, sheet.nrows):
        data.append(sheet.row_values(i))
    return data




def export_excel(table_name):
    import pymysql
    host, user, passwd, db = '127.0.0.1', 'root', 'root', 'test'
    conn = pymysql.connect(user=user,host=host,port=3306,passwd=passwd,db=db,charset='utf8')
    cur = conn.cursor()  # 建立游标
    sql = 'select * from %s;' %table_name
    cur.execute(sql)  # 执行mysql
    fileds = [filed[0] for filed in cur.description]  # 列表生成式，所有字段
    all_data = cur.fetchall() #所有数据
    #写excel
    book = xlwt.Workbook() #先创建一个book
    sheet = book.add_sheet('sheet1') #创建一个sheet表
    # col = 0
    # for field in fileds: #写表头的
    #     sheet.write(0, col, field)
    #     col += 1
    #enumerate自动计算下标
    for col, field in enumerate(fileds): #跟上面的代码功能一样
        sheet.write(0, col, field)

    #从第一行开始写
    row = 1 #行数
    for data in all_data:  #二维数据，有多少条数据，控制行数
        for col, field in enumerate(data):  #控制列数
            sheet.write(row, col, field)
        row += 1 #每次写完一行，行数加1
    book.save('%s.xls' %table_name) #保存excel文件

export_excel('app_student')


if __name__ == '__main__':
    print(read('D:/读取excel存储到mysql.xlsx'))














