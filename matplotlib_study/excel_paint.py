# coding=utf-8
import pandas as pd
import matplotlib as mb
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
xls = pd.read_excel("学生期末成绩统计表.xlsx")
date = xls #存储数据
myData1 = date["语文"]
myData2 = date["数学"]
myData3 = date["英语"]

l1, = plt.plot(myData1)# 默认折线、实线
l2, = plt.plot(myData2, color="blue", linewidth=1.5, linestyle="-") # 蓝色，1.5宽，线段
l3, = plt.plot(myData3, 'r', linewidth=2.5, linestyle ='--')# 红色，2.5宽，虚线
plt.legend(handles=[l1, l2, l3], labels=['语文', '数学', '英语'], loc='best')
plt.show()