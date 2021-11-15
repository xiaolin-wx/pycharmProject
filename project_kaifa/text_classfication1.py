import jieba
import jieba.analyse
import warnings
import pymysql
import random
import traceback
from scipy.special import comb
import pandas as pda
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
warnings.filterwarnings("ignore")

# 设置数据库的连接
# conn = pymysql.connect(host="localhost",user="root",passwd="13820541017",db="jobdata",charset="utf8")

# 获取数据
car_news = pda.read_csv("data1/car_news.csv",encoding="utf-8")
car_news = car_news.dropna()

finance_news = pda.read_csv("data1/finance_news.csv",encoding="utf-8")
finance_news = finance_news.dropna()

home_news = pda.read_csv("data1/home_news.csv",encoding="utf-8")
home_news = home_news.dropna()

international_news = pda.read_csv("data1/international_news.csv",encoding="utf-8")
international_news = international_news.dropna()

military_news = pda.read_csv("data1/military_news.csv",encoding="utf-8")
military_news = military_news.dropna()

society_news = pda.read_csv("data1/society_news.csv",encoding="utf-8")
society_news = society_news.dropna()

sports_news = pda.read_csv("data1/sports_news.csv",encoding="utf-8")
sports_news = sports_news.dropna()

technology_news = pda.read_csv("data1/technology_news.csv",encoding="utf-8")
technology_news = technology_news.dropna()


#将取出的数据各提取出20000个，以保证各个样本的数量相同
car_news = car_news.content.values.tolist()[1000:21000]
finance_news = finance_news.content.values.tolist()[1000:21000]
home_news = home_news.content.values.tolist()[:20000]
international_news = international_news.content.values.tolist()[:20000]
military_news = military_news.content.values.tolist()[:20000]
society_news = society_news.content.values.tolist()[:20000]
sports_news = sports_news.content.values.tolist()[:20000]
technology_news = technology_news.content.values.tolist()[:20000]

print(car_news[10])
print(finance_news[10])
print(home_news[12])
print(international_news[13])
print(military_news[2])
print(society_news[13])
print(sports_news[14])
print(technology_news[14])

#取出停用词，以便后续去除停用词做准备
stopwords = [line.strip() for line in open("data1/stopwords.txt","r",encoding="utf-8").readlines()]
# print(stopwords)

#去除停用词并进行分词
def preprosess_text(content_line,sentences,categroy):
    for line in content_line:
        try:
            segs = jieba.lcut(line)
            segs = filter(lambda x:len(x)>1,segs)
            segs = filter(lambda x:x not in stopwords,segs)
            sentences.append((" ".join(segs),categroy))
        except Exception:
            # print(line)
            print("有异常............................")
            continue
        # 构建训练集
sentences = []
preprosess_text(car_news, sentences, 'car_news')
preprosess_text(finance_news, sentences, 'finance_news')
preprosess_text(home_news, sentences, 'home_news')
preprosess_text(international_news, sentences, 'international_news')
preprosess_text(military_news, sentences, 'military_news')
preprosess_text(society_news, sentences, 'society_news')
preprosess_text(technology_news, sentences, 'technology_news')

# print(sentences)
#为了使朴素贝叶斯能够训练分类，现将所有的数据进行打乱排序.shuffle()将元素进行随机排序
random.shuffle(sentences)

#将数据分成训练集和测试集，使用zip()函数，他时拉链函数。zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
#如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
x,y = zip(*sentences)
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1234)
# print(len(x_train))
# print(len(x_test))

class TextClassfilter():
    def __init__(self,classfiler=MultinomialNB()):
        self.classfiler = classfiler
        self.vectorize = CountVectorizer(analyzer='word',ngram_range=(1,10),max_features=40000)
    def feartures(self,X):
        return self.vectorize.transform(X)
    def fit(self,X,y):
        self.vectorize.fit(X)
        self.classfiler.fit(self.feartures(X),y)
    def predict(self,x):
        return self.classfiler.predict(self.feartures([x]))
    def score(self,X,y):
        return self.classfiler.score(self.feartures(X),y)

text_classfiler = TextClassfilter()
text_classfiler.fit(x_train,y_train)

while True:
    # 用户自主输入文本
    sentence = input("请输入文本:")

    # 对文本进行切词，并去除停用词
    sentences = []

    print("正在预测..........")
    segs = jieba.lcut(sentence)
    segs = filter(lambda x:len(x)>1,segs)
    segs = filter(lambda x:x not in stopwords,segs)
    sentences.append((" ".join(segs)))

    result = text_classfiler.predict(sentences[0])
    print(sentence+"------------------"+result[0])