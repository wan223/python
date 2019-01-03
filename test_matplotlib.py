# import random
# import matplotlib.pyplot as plt
# count = 1024
# # 随机参数1024个随机点的X坐标值
# X = [random.random() * 100 for i in range(count)]
# # 随机参数1024个随机点的Y坐标值
# Y = [random.random() * 100 for i in range(count)]
# # 绘制1024个随机点
# plt.scatter(X,Y)
# # 显示绘制的随机点
# plt.show()

#
# import matplotlib.pyplot as plt
# # 绘制柱状图，[1980,1985,1990,1995]表示X坐标序列
# # [1000,3000,4000,5000]表示Y坐标序列，width表示柱的宽度
# plt.bar([1980,1985,1990,1995],[1000,3000,4000,5000],width = 1)
# # 显示状态图
# plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt
# # 产生100个正态分布的随机数
# data = np.random.randn(100)
# print(data)
# # 计算100个随机数的平均数
# print(np.average(data))
# # 在同一个窗口创建两个二维坐标系，左侧的坐标系显示直方图，右侧的坐标系显示盒状图
# fig,(ax1,ax2) = plt.subplots(1,2,figsize=(8,8))
# # 绘制直方图
# ax1.hist(data,100)
# # 绘制盒状图
# ax2.boxplot(data)
# # 显示直方图和盒状图
# plt.show()


# import matplotlib.pyplot as plt
# data = [5,67,23,43,64]
# # 绘制饼图
# plt.pie(data)
# # 显示饼图
# plt.show()

# from pandas import *
# from matplotlib.pyplot import *
# import sqlite3
# import sqlalchemy
# engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
# rcParams['font.sans-serif'] = ['SimHei']
# options.display.float_format = '{:,.2f}%'.format
# sales = read_sql('select source,color1 from t_sales',engine)
# # 按color1分组，并统计每组的数量
# color1Count = sales.groupby('color1')['color1'].count()
# # 统计总销量
# color1Total = color1Count.sum()
# print(color1Total)
# color1 = color1Count.to_frame(name='销量')
# print(color1)
# color1.insert(0,'比例', 100 * color1Count / color1Total)
# color1.index.names=['颜色']
# color1 = color1.sort_values(['销量'], ascending=[0])
# print(color1)
# n = 1200
# # 销量小于等于1200都属于“其他”分组
# others = DataFrame([color1[color1['销量'] <= n].sum()],index=MultiIndex(levels=[['其他']],labels=[[0]]))
# # 将others添加到原来的记录集中
# color1 = color1[color1['销量']>n].append(others)
# print(color1)
# # 将索引转换为在饼图周围显示的标签
# labels = color1.index.tolist()
# pie(color1['销量'],labels=labels,autopct='%.2f%%')
# legend()
# axis('equal')
# title('按胸罩颜色统计的比例')
# show()



# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([3,5,7,6,2,6,10,15])
# plt.plot(x,y,'r')# 折线 1 x 2 y 3 color
# plt.plot(x,y,'g',lw=10)# 4 line w
# # 折线 饼状 柱状
# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([13,25,17,36,21,16,10,15])
# plt.bar(x,y,0.2,alpha=1,color='b')# 5 color 4 透明度 3 0.9
# plt.show()


# -*- coding: utf-8 -*-
"""
简单图形绘制

"""

import matplotlib.pyplot as plt
import numpy as np

#从-1-----1之间等间隔采66个数.也就是说所画出来的图形是66个点连接得来的
#注意：如果点数过小的话会导致画出来二次函数图像不平滑
x = np.linspace(-1, 1,66)
# 绘制y=2x+1函数的图像
y = 2 * x + 1
plt.plot(x, y)
plt.show()

# 绘制x^2函数的图像
y = x**2
plt.plot(x, y)
plt.show()










