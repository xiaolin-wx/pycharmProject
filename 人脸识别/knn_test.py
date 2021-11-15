import creatKnn
from numpy import *
# 生成数据集和类别标签
dataSet, labels = creatKnn.createDataSet()
# 定义一个未知类别的数据
testX = array([1.2, 1.0])
k = 3
# 调用分类函数对未知数据分析
outputLabel = creatKnn.kNNClassify(testX, dataSet, labels, 3)
print("Yours input is:", testX, "and classifind to class:", outputLabel)

testX = array([0.1, 0.3])
outputLabel = creatKnn.kNNClassify(testX, dataSet, labels, 3)
print("Yours input is:", testX, "and classifind to class:", outputLabel)