from numpy import *

# 创建一个数据集，包含2个类别共四个样本
def createDataSet():
    # 生成一个矩阵，每行表示一个样本
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    # 4个样本分别所属的类别
    labels = ['A', 'A', 'B', 'B']
    return group, labels

# KNN分类算法函数的定义
def kNNClassify(newInput, dataSet, labels, k):
    # print(dataSet)
    numSamples = dataSet.shape[0]   #shape[0]表示行数

    diff = tile(newInput, (numSamples, 1)) - dataSet
    # print(diff)
    squaredDiff = diff ** 2 #将差值平方
    squaredDist = sum(squaredDiff, axis=1) #按行累加
    distance = squaredDist ** 0.5  #将差值平方和求开方，即得距离

    sortedDistIndices = argsort(distance)
    classCount = {}
    for i in range(k):
        # step :3 选择K个最近邻
        voteLabel = labels[sortedDistIndices[i]]

        # step :4 计算k个最近邻中各类别出现的次数
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    # step :5 返回出现次数最多的标签
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex
