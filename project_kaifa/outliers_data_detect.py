import pandas as pd
import matplotlib.pyplot as plt
#主要用来设置坐标的刻度
from matplotlib.pyplot import MultipleLocator

# 设置图像的字体以及设置图像显示正负号
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 地址列表
table_list = ["data_classfication/finance.xlsx","data_classfication/medical.xlsx","data_classfication/computer.xlsx","data_classfication/electronics.xlsx","data_classfication/real_estate.xlsx","data_classfication/service.xlsx","data_classfication/transportation.xlsx"]
data_name = ["finance","medical","computer","education","electronics","real_estate","service","transportation"]
figure_lable = ["金融类工作异常值检测","医疗类工作异常值检测","计算机类异常值检测","教育类工作异常值检测","电子类工作异常值检测","房地产类工作异常值检测","服务行业工作异常值检测","交通运输类工作异常值检测"]
# 循环遍历所有的数据表
for table in table_list:
    data_name[table_list.index(table)] = pd.read_excel(table,index_col="min_salary")
    print(data_name[table_list.index(table)].describe())

    # 创建画布
    figure = plt.figure(num=figure_lable[table_list.index(table)])
    # 给图像设置一个标题
    plt.title(figure_lable[table_list.index(table)],fontsize=14,color="blue")

    # 设置一些，x轴y轴的刻度
    y_major_locator=MultipleLocator(30000)
    ax=plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    plt.ylim([-550000,550000])

    # 画箱型图，直接采用DataFrame的方法
    p1 = data_name[table_list.index(table)].boxplot(return_type='dict',sym='r')

    # fliers即为异常值的标签
    x = p1['fliers'][0].get_xdata()
    y = p1['fliers'][0].get_ydata()

    # y的值由大到小的顺序进行排序
    y.sort()

    plt.ylabel("工资分布",fontsize=14,color="blue")
    plt.xlabel("字段名称",fontsize=14,color="blue")

    # 使用annotate来对图像进行添加注释
    for i in range(len(x)):
        if i>0:
            plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
        else:
            plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))

plt.show()
