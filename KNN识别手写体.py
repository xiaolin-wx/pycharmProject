from numpy import *
import operator
from os import listdir  # 用于获取目录中的文件名


# 将32*32的二进制图像矩阵转换为1*1024的向量
def image2vector(filename):
    returnVector = zeros((1, 1024))
    with open(filename) as file:
        for i in range(32):
            line = file.readline()
            for j in range(32):
                returnVector[0, 32 * i + j] = int(line[j])
    return returnVector


# k-近邻算法
def classify(inX, dataSet, labels, k):
    num = dataSet.shape[0]  # 数据集中的样本个数
    diffMatrix = tile(inX, (num, 1)) - dataSet  # 将测试向量转换为dataSet的同型矩阵并与dataSet做差
    # 使用欧式距离公式求测试样本与训练集中样本的距离
    sqDiffMatrix = diffMatrix ** 2
    sqDistance = sqDiffMatrix.sum(axis=1)
    distance = sqDistance ** 0.5
    sortedDistIndicies = distance.argsort()  # 对距离进行排序，返回排序后的索引值
    classCount = {}
    for i in range(k):
        label = labels[sortedDistIndicies[i]]
        classCount[label] = classCount.get(label, 0) + 1  # 若字典中存在label键，则对应的值+1，如果不存在，则添加这个键设置为0并+1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # 按照字典中的值对字典进行降序排列
    return sortedClassCount[0][0]


# 手写数字识别的测试代码
def handWritingClassTest():
    labels = []
    trainingFileList = listdir('trainingDigits')  # 获取训练集目录下的文件名
    m = len(trainingFileList)  # 计算训练样本个数
    dataSet = zeros((m, 1024))  # 初始化数据集
    for i in range(m):
        fileName = trainingFileList[i]
        number = int(fileName.split('_')[0])  # number为每个样本的分类
        labels.append(number)
        dataSet[i, :] = image2vector('trainingDigits\%s' % fileName)
    testFileList = listdir('testDigits')
    mTest = len(testFileList)
    error = 0.0
    for i in range(mTest):
        fileName = testFileList[i]
        number = int(fileName.split('_')[0])
        testVector = image2vector('testDigits\%s' % fileName)
        resultNumber = classify(testVector, dataSet, labels, 3)  # 使用算法估计样本所属类别
        if number != resultNumber:  # 算法结果与样本的实际分类做对比
            error += 1.0
    print('the total number of errors is:', error)
    print('the total error rate is:', error / mTest)


handWritingClassTest()