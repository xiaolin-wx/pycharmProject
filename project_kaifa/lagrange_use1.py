# 导入相应的包
import numpy as npy
import pandas as pda
import warnings
from scipy.interpolate import lagrange      #导入拉格朗日插值函数

# 设置忽略警告信息
warnings.filterwarnings("ignore")

# 定义文件列表，将所有要处理的文件都放入到一个列表当中
# table_list = ['data_classfication/computer.xlsx','data_classfication/education.xlsx','data_classfication/electronics.xlsx','data_classfication/finance.xlsx','data_classfication/medical.xlsx','data_classfication/real_estate.xlsx','data_classfication/service.xlsx','data_classfication/transportation.xlsx']
table_list = ['medical.xlsx']
# 循环遍历一个列表，运行程序之前首先创建一个data_processed文件夹，然后将处理好的文件都放入此文件夹当中
for k1 in range(len(table_list)):
    # 定义输出文件的路径
    # outputfile = "data_processed/{}".format(table_list[k1][19:])
    outputfile = "medical222.xlsx"
    print(outputfile)
    # 依次读取每个表中的数据
    data = pda.read_excel(table_list[k1])

    # 过滤异常值
    # data2[u'salary'][(data2[u'salary']<max_salary[k1])|(data2[u'salary']>min_salary[k1])] = None

    # 构建拉格朗日函数，使他能够进行正确的插值
    def ployinterp_column(s,n,k=1):
        y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]
        y=y[y.notnull()]
        return int(abs(lagrange(y.index,list(y))(n)))
    k=0

    # 依次遍历excel表格中的每一行数据
    for i in data.columns:
        for j in range(len(data)):
            # 如果遇到salary的值为空，就进行插值
            if (data[i].isnull())[j]:
                # print(data2[i])
                data[i][j] = ployinterp_column(data[i],j)
                print(data[i][j])
                k+=1

    # 最后将插值的结果存放到指定的文件夹中
    data.to_excel(outputfile)
    print("总处理了"+str(k)+"条缺失值.............................")
