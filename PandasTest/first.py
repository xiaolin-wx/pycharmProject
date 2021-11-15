import numpy as np
import pandas as pd

# 读取本地文件
dataframe = pd.read_excel("数据分析与应用技术.xls")
# print(dataframe)
print(dataframe.describe())
print(dataframe.iloc[:3])

# 读取远程文件            文件路径
# web_data = pd.read_excel("")

# print(dataframe.head())

# 创建 DataFrame 对象
data = pd.DataFrame()
data["name"] = ["user1", "user2"]
data["age"] = [12, 23]
data["sex"] = ["man", "women"]

print(data.shape[1])
# 查询某行数据
print(data.iloc[1])

print(dataframe[dataframe["序号"] >= 12])

print(dataframe[dataframe["性别"] >= "男"])
print(dataframe["性别"].replace("男", "man"))

print(dataframe["学号"].max())
print(dataframe["学号"].min())
print(dataframe["学号"].mean())
print(dataframe["学号"].sum())
print(dataframe["学号"].count())
print(dataframe["学号"].var())