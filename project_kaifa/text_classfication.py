import jieba
import random
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# 读取csv表格数据
df_technology = pd.read_csv("data2/technology_news.csv",encoding="utf-8")
# 去除空行，在爬虫的时候有些行可能是空的，使用这条语句进行去重
df_technology = df_technology.dropna()

df_car = pd.read_csv("data2/car_news.csv",encoding="utf-8")
# 去除空行，在爬虫的时候有些行可能是空的，使用这条语句进行去重
df_car = df_car.dropna()

df_entertainment = pd.read_csv("data2/entertainment_news.csv",encoding="utf-8")
# 去除空行，在爬虫的时候有些行可能是空的，使用这条语句进行去重
df_entertainment = df_entertainment.dropna()

df_military = pd.read_csv("data2/military_news.csv",encoding="utf-8")
# 去除空行，在爬虫的时候有些行可能是空的，使用这条语句进行去重
df_military = df_military.dropna()

df_sports = pd.read_csv("data2/sports_news.csv",encoding="utf-8")
# 去除空行，在爬虫的时候有些行可能是空的，使用这条语句进行去重
df_sports = df_sports.dropna()

# 将各个类别的数据各取出20000条
technology = df_technology.content.values.tolist()[1000:21000]
car = df_car.content.values.tolist()[1000:21000]
entertainment = df_entertainment.content.values.tolist()[:20000]
military = df_military.content.values.tolist()[:20000]
sports = df_sports.content.values.tolist()[:20000]

# 取出停用词，以便后续去除停用词做准备
stopwords = [line.strip() for line in open("data2/stopwords.txt","r",encoding="utf-8").readlines()]
print(stopwords)

# 定义函数用来数据预处理
def preprocess_text(content_lines,sentences,category):
    for line in content_lines:
        try:
            segs = jieba.lcut(line)
            segs = filter(lambda x:len(x)>1,segs)

            # 做一个停用词的过滤
            segs = filter(lambda x:x not in stopwords,segs)

            # 将所有分好词以后的句子做一个拼接，然后指定其类别
            sentences.append((" ".join(segs),category))
        except:
            print(line)
            continue

# 生成训练数据
sentences = []

preprocess_text(technology, sentences,'technology')
preprocess_text(car, sentences,'car')
preprocess_text(entertainment, sentences,'entertainment')
preprocess_text(military, sentences,'military')
preprocess_text(sports, sentences,'sports')

# 将所有数据的顺序打乱，这样就可以生成可靠的训练数据
random.shuffle(sentences)

for sentence in sentences:
    print(sentence[0],sentence[1])

# 将所有的数据划分为训练集和测试集
x,y = zip(*sentences)
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1234)

# 在降噪数据上抽取出有用的特征，这里对文本进行词袋模型特征
vec = CountVectorizer(analyzer='word',ngram_range=(1,4),max_features=4000,)
vec.fit(x_train)

def get_features(x):
    vec.transform(x)

# 构建朴素贝叶斯分类器
classifier = MultinomialNB()
# 使用朴素贝叶斯对文本进行训练
classifier.fit(vec.transform(x_train),y_train)

# 查看训练的准确率
print(classifier.score(vec.transform(x_test),y_test))

