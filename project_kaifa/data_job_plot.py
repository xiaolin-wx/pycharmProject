import pandas as pda
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

# 获取数据
computer = pda.read_excel("data_processed/computer.xlsx",encoding="utf-8")
education = pda.read_excel("data_processed/education.xlsx",encoding="utf-8")
electronics = pda.read_excel("data_processed/electronics.xlsx",encoding="utf-8")
finance = pda.read_excel("data_processed/finance.xlsx",encoding="utf-8")
medical = pda.read_excel("data_processed/medical.xlsx",encoding="utf-8")
real_estate = pda.read_excel("data_processed/real_estate.xlsx",encoding="utf-8")
service = pda.read_excel("data_processed/service.xlsx",encoding="utf-8")
transportation = pda.read_excel("data_processed/transportation.xlsx",encoding="utf-8")

# 定义几个列表用来存放不同的数值和数值出现的个数
computer_diff_data = []
education_diff_data = []
electronics_diff_data = []
finance_diff_data = []
medical_diff_data = []
real_estate_diff_data = []
service_diff_data = []
transportation_diff_data = []

# 统计不同元素出现的个数
computer_number = []
education_number = []
electronics_number = []
finance_number = []
medical_number = []
real_estate_number = []
service_number = []
transportation_number = []

# 将取出的数据各提取出45000条工资数据，以保证各个样本的数量相同
computer_data = computer.salary.values.tolist()[1000:50000]
education_data = education.salary.values.tolist()[:49000]
electronics_data = electronics.salary.values.tolist()[:49000]
finance_data = finance.salary.values.tolist()[:49000]
medical_data = medical.salary.values.tolist()[:49000]
real_estate = real_estate.salary.values.tolist()[:49000]
service_data = service.salary.values.tolist()[:49000]
transportation_data = transportation.salary.values.tolist()[:49000]

# 统计每个元素出现的个数
result1 = Counter(computer_data)
result2 = Counter(education_data)
result3 = Counter(electronics_data)
result4 = Counter(finance_data)
result5 = Counter(medical_data)
result6 = Counter(real_estate)
result7 = Counter(service_data)
result8 = Counter(transportation_data)

# 分别打印它的键和值
for item in result1.keys():
    computer_diff_data.append(item)
computer_diff_data.sort()

for item in result2.keys():
    education_diff_data.append(item)
education_diff_data.sort()

for item in result3.keys():
    electronics_diff_data.append(item)
electronics_diff_data.sort()

for item in result4.keys():
    finance_diff_data.append(item)
finance_diff_data.sort()

for item in result5.keys():
    medical_diff_data.append(item)
medical_diff_data.sort()

for item in result6.keys():
    real_estate_diff_data.append(item)
real_estate_diff_data.sort()

for item in result7.keys():
    service_diff_data.append(item)
service_diff_data.sort()

for item in result8.keys():
    transportation_diff_data.append(item)
transportation_diff_data.sort()

# 依次将各个元素出现的个数添加到列表中
for i in computer_diff_data:
    computer_number.append(result1[i])

for i in education_diff_data:
    education_number.append(result2[i])

for i in finance_diff_data:
    electronics_number.append(result3[i])

for i in medical_diff_data:
    finance_number.append(result4[i])

for i in real_estate_diff_data:
    medical_number.append(result5[i])

for i in electronics_diff_data:
    real_estate_number.append(result6[i])

for i in service_diff_data:
    service_number.append(result7[i])

for i in transportation_diff_data:
    transportation_number.append(result8[i])

plt.plot(computer_diff_data,computer_number,label="计算机类型工资分布")
plt.plot(education_diff_data,education_number,label="教育类型工资分布")
plt.plot(finance_diff_data,electronics_number,label="金融类型工资分布")
plt.plot(medical_diff_data,finance_number,label="医疗类型工资分布")
plt.plot(real_estate_diff_data,medical_number,label="房地产类型工资分布")
plt.plot(electronics_diff_data,real_estate_number,label="电子类型工资分布")
plt.plot(service_diff_data,service_number,label="服务类型工资分布",marker=".",ms="4")
# plt.plot(transportation_diff_data,transportation_number,label="交通运输类型工资分布")

plt.legend()
plt.savefig("classfication.png")
plt.show()


