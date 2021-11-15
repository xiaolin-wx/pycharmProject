# 导入相应的包
import numpy as npy
import pandas as pda
import warnings
from scipy.interpolate import lagrange      #导入拉格朗日插值函数

# 设置忽略警告信息
warnings.filterwarnings("ignore")

# 定义文件列表，将所有要处理的文件都放入到一个列表当中
# file_list = ["data2/algorithm_engineer2.xls"]
file_list = ["data2/education1.xls","data2/mechine_learning1.xls","data2/operate1.xls","data2/operation_maintenance1.xls","data2/production_manager1.xls","data2/ui_design1.xls"]

# 循环遍历一个列表，运行程序之前首先创建一个data_processed文件夹，然后将处理好的文件都放入此文件夹当中
for item in file_list:

    # 定义输出文件的路径
    outputfile = "data_processed/{}".format(item[5:])
    print(outputfile)
    # 依次读取每个表中的数据
    data = pda.read_excel(item)

    # 构建拉格朗日函数，使他能够进行正确的插值
    def ployinterp_column(s,n,k=2):
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
                k+=1

    # 最后将插值的结果存放到指定的文件夹中
    data.to_excel(outputfile)
    print("总处理了"+str(k)+"条缺失值.............................")
