import numpy as np
import pandas as pd

# 统计列表中元素出现的个数
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# 创建一张画布
figure = plt.figure(num="工资分布图")

# 设置图像显示中文和负号
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

# 设置图像标题
plt.title("工资分布图",fontsize=14,color="red")
plt.xlabel("工资",fontsize=14,color="red")
plt.ylabel("所占比重",fontsize=14,color="red")

# 分别设置x轴和y轴的刻度
x_major_locator = MultipleLocator(3000)
y_major_locator = MultipleLocator(2)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

# 分别设置x轴和y轴的刻度范围
plt.xlim([0,55000])
plt.ylim([0,300])

# 定义列表，用来存放工资的数据
salary_data = []
android_data = []
big_data = []
edu_data = []
mech_data = []
web_data = []
oper_data = []
pro_data = []
ui_data = []

# 定义一个列表用来存放去除重复数据的列表
diff_data = []
android_diff_data = []
big_diff_data = []
edu_diff_data = []
mech_diff_data = []
oper_diff_data = []
pro_diff_data = []
ui_diff_data = []

# 定义一个列表用来存放数据出现的次数列表
diff_data_number = []
android_diff_data_number = []
big_diff_data_number = []
edu_diff_data_number = []
mech_diff_data_number = []
oper_diff_data_number = []
pro_diff_data_number = []
ui_diff_data_number = []

# 读取excel表格的数据
data = pd.read_excel("data_processed/algorithm_engineer1.xls",usecols="D")
data = data.values.tolist()

android_development1 = pd.read_excel("data_processed/android_development1.xls",usecols="D")
android_development1 = android_development1.values.tolist()

big_data1 = pd.read_excel("data_processed/big_data1.xls",usecols="D")
big_data1 = big_data1.values.tolist()

education1 = pd.read_excel("data_processed/education1.xls",usecols="D")
education1 = education1.values.tolist()

mechine_learning1 = pd.read_excel("data_processed/mechine_learning1.xls",usecols="D")
mechine_learning1 = mechine_learning1.values.tolist()

operate1 = pd.read_excel("data_processed/operate1.xls",usecols="D")
operate1 = operate1.values.tolist()

operation_maintenance1 = pd.read_excel("data_processed/operation_maintenance1.xls",usecols="D")
operation_maintenance1 = operation_maintenance1.values.tolist()

production_manager1 = pd.read_excel("data_processed/production_manager1.xls",usecols="D")
production_manager1 = production_manager1.values.tolist()

ui_design1 = pd.read_excel("data_processed/ui_design1.xls",usecols="D")
ui_design1 = ui_design1.values.tolist()

# 循环遍历所有的数据，然后将其加入到相应的列表中
for i in range(len(data)):
    salary_data.append(int(data[i][0]))

for i in range(len(android_development1)):
    android_data.append(int(android_development1[i][0]))

for i in range(len(big_data1)):
    big_data.append(int(big_data1[i][0]))

for i in range(len(education1)):
    edu_data.append(int(education1[i][0]))

for i in range(len(mechine_learning1)):
    mech_data.append(int(mechine_learning1[i][0]))

for i in range(len(operate1)):
    web_data.append(int(operate1[i][0]))

for i in range(len(operation_maintenance1)):
    oper_data.append(int(operation_maintenance1[i][0]))

for i in range(len(production_manager1)):
    pro_data.append(int(production_manager1[i][0]))

for i in range(len(ui_design1)):
    ui_data.append(int(ui_design1[i][0]))

# 统计每个元素出现的个数
result1 = Counter(salary_data)
result2 = Counter(android_data)
result3 = Counter(big_data)
result4 = Counter(edu_data)
result5 = Counter(mech_data)
result6 = Counter(web_data)
result7 = Counter(oper_data)
result8 = Counter(pro_data)
result9 = Counter(ui_data)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)

# 分别打印它的键和值
for item in result1.keys():
    diff_data.append(item)
diff_data.sort()

for item in result2.keys():
    android_diff_data.append(item)
android_diff_data.sort()

for item in result3.keys():
    big_diff_data.append(item)
big_diff_data.sort()

for item in result4.keys():
    edu_diff_data.append(item)
edu_diff_data.sort()

for item in result5.keys():
    mech_diff_data.append(item)
mech_diff_data.sort()

for item in result6.keys():
    oper_diff_data.append(item)
oper_diff_data.sort()

for item in result7.keys():
    pro_diff_data.append(item)
pro_diff_data.sort()

for item in result8.keys():
    ui_diff_data.append(item)
ui_diff_data.sort()

print(diff_data)
print(android_diff_data)
print(big_diff_data)
print(edu_diff_data)
print(mech_diff_data)
print(oper_diff_data)
print(pro_diff_data)
print(ui_diff_data)

# 依次将各个元素出现的个数添加到列表中
for i in diff_data:
    diff_data_number.append(result1[i])

for i in android_diff_data:
    android_diff_data_number.append(result2[i])

for i in big_diff_data:
    big_diff_data_number.append(result3[i])

for i in edu_diff_data:
    edu_diff_data_number.append(result4[i])

for i in mech_diff_data:
    mech_diff_data_number.append(result5[i])

for i in oper_diff_data:
    oper_diff_data_number.append(result6[i])

for i in pro_diff_data:
    pro_diff_data_number.append(result7[i])

for i in ui_diff_data:
    ui_diff_data_number.append(result8[i])

print(diff_data_number)
print(android_diff_data_number)
print(big_diff_data_number)
print(edu_diff_data_number)
print(mech_diff_data_number)
print(oper_diff_data_number)
print(pro_diff_data_number)
print(ui_diff_data_number)

plt.plot(diff_data,diff_data_number,color="#121a2a",label="算法工资类型")
plt.plot(android_diff_data,android_diff_data_number,color="#ffe600",label="安卓工资类型")
plt.plot(big_diff_data,big_diff_data_number,color="#009ad6",label="大数据工资类型")
plt.plot(edu_diff_data,edu_diff_data_number,color="#130c0e",label="教育工资类型")
plt.plot(mech_diff_data,mech_diff_data_number,color="red",label="机器学习工资类型")
plt.plot(oper_diff_data,oper_diff_data_number,color="yellow",label="运维工资类型")
plt.plot(pro_diff_data,pro_diff_data_number,color="#d71345",label="产品经理工资类型",marker=".",ms="15")
plt.plot(ui_diff_data,ui_diff_data_number,color="#412f1f",label="UI设计工资类型")

plt.legend()
plt.savefig("classfication.png")
plt.show()