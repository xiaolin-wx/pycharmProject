#导入相应的包
import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

#加载数据
fashion_mnist = keras.datasets.fashion_mnist
#训练集和测试集的划分
(train_images, train_lables), (test_images, test_lables) = fashion_mnist.load_data()

#进行数据预处理,将每个像素点压缩在0~1之间
#好处:1）节省运算量
train_images = train_images/255.0
test_images = test_images/255.0

#搭建简单的神经网络
def creat_model():
    #创建神经网络模型
    model = tf.keras.models.Sequential([
        #输入层
        keras.layers.Flatten(input_shape=(28,28)),
        #一个隐藏层
        keras.layers.Dense(128,activation="relu"),
        #输出层
        keras.layers.Dense(10),

    ])
    # 编译模型
    model.compile(
        #优化器
        optimizer="adam",
        #损失值  不可和原来的数据形同，如果发生这件事会发生过拟合
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[tf.metrics.SparseCategoricalAccuracy()]
    )
    #返回模型
    return model

#构建模型
new_model = creat_model()

#训练模型  epochs——训练几次
new_model.fit(train_images, train_lables, epochs=250)

#保存模型
new_model.save("model/my_model10.h5")

