import pandas as pda
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# 指定三个列表，分别用来存放工作类别，学历要求以及工作地点
table_list = ["computer","education","electronics","finance","medical","real_estate","service","transportation",]
label_list = ["计算机类","教育类","电子类","金融类","医疗类","房地产类","服务类","运输类",]
address_list = ["北京","上海","广州","深圳","杭州","武汉","成都","重庆","西安"]

# 循环遍历三张列表，用来存放地址信息
for k1 in range(len(table_list)):
    # 创建一张画布
    figure = plt.figure(num=str(table_list[k1]),figsize=(10,6))

    # 设置图像显示中文和负号
    plt.rcParams['font.sans-serif'] = ['']
    plt.rcParams['axes.unicode_minus'] = False

    # 设置图像标题
    plt.title(str(label_list[k1]), fontsize=14, color="blue")
    plt.xlabel("工资", fontsize=14, color="blue")
    plt.ylabel("所占比重", fontsize=14, color="blue")

    for k2 in range(len(address_list)):
        print("========================>"+table_list[k1]+address_list[k2]+".xlsx <================================")

        # 指定列表的名字
        data_name = table_list[k1]+address_list[k2]
        data_name_data = table_list[k1]+address_list[k2]+"_data"
        job_list_name = table_list[k1]+address_list[k2]
        diff_list_name = table_list[k1]+address_list[k2]+"_diff_data"
        diff_list_number = table_list[k1] + address_list[k2] + "_diff_data_number"
        result = address_list[k2]+"_result"

        # 用来存放所有的工资数据
        vars()[job_list_name] = []
        # 用来存放所有工资数据去重后的列表
        vars()[diff_list_name] = []
        # 用来存放所有工资中不同工资的个数
        vars()[diff_list_number] = []

        # 依次读取每个表中的数据
        vars()[data_name] = pda.read_excel("data_address_processed/"+table_list[k1]+address_list[k2]+".xlsx")

        # 将取出的数据各提取出5000条工资数据，以保证各个样本的数量相同
        vars()[data_name_data] = vars()[data_name].salary.values.tolist()[0:1200]

        # 统计列表中每个元素出现的个数
        vars()[result] = Counter(vars()[data_name_data])

        # 分别打印每个列表的键和值
        for item in vars()[result].keys():
            vars()[diff_list_name].append(item)
        vars()[diff_list_name].sort()

        # 依次将各个元素出现的个数添加到列表中
        for i in vars()[diff_list_name]:
            vars()[diff_list_number].append(vars()[result][i])

        plt.plot(vars()[diff_list_name],vars()[diff_list_number],label=str(address_list[k2]))

    plt.legend()
    plt.savefig("img_data/"+table_list[k1]+".png")

plt.show()