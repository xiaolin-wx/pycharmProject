import jieba
import jieba.analyse
import warnings
import pymysql
import random
import traceback
import pandas as pda
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
warnings.filterwarnings("ignore")

# 设置数据库的连接
conn1 = pymysql.connect(host="localhost",user="root",passwd="13820541017",db="jobdata",charset="utf8")
conn = pymysql.connect(host="localhost",user="root",passwd="13820541017",db="job_calssfication",charset="utf8")

# 获取数据
android_development = pda.read_excel("data2/android_development.xls",encoding="utf-8")
android_development = android_development.dropna()

big_data = pda.read_excel("data2/big_data.xls",encoding="utf-8")
big_data = big_data.dropna()

deep_learning = pda.read_excel("data2/deep_learning.xls",encoding="utf-8")
deep_learning = deep_learning.dropna()

education = pda.read_excel("data2/education.xls",encoding="utf-8")
education = education.dropna()

mechine_learning = pda.read_excel("data2/mechine_learning.xls",encoding="utf-8")
mechine_learning = mechine_learning.dropna()

nature_language_process = pda.read_excel("data2/nature_language_process1.xls",encoding="utf-8")
nature_language_process = nature_language_process.dropna()

operate = pda.read_excel("data2/operate.xls",encoding="utf-8")
operate = operate.dropna()

operation_maintenance = pda.read_excel("data2/operation_maintenance.xls",encoding="utf-8")
operation_maintenance = operation_maintenance.dropna()

production_manager = pda.read_excel("data2/production_manager.xls",encoding="utf-8")
production_manager = production_manager.dropna()

ui_design = pda.read_excel("data2/ui_design.xls",encoding="utf-8")
ui_design = ui_design.dropna()

#将取出的数据各提取出300个，以保证各个样本的数量相同
android_development = android_development.job_request.values.tolist()
big_data = big_data.job_request.values.tolist()
deep_learning = deep_learning.job_request.values.tolist()
education = education.job_request.values.tolist()
mechine_learning = mechine_learning.job_request.values.tolist()
nature_language_process = nature_language_process.job_request.values.tolist()
operate = operate.job_request.values.tolist()
operation_maintenance = operation_maintenance.job_request.values.tolist()
production_manager = production_manager.job_request.values.tolist()
ui_design = ui_design.job_request.values.tolist()

print(android_development[10])
print(big_data[10])
print(deep_learning[12])
print(education[13])
print(mechine_learning[2])
print(nature_language_process[13])
print(operate[14])

#取出停用词，以便后续去除停用词做准备
stopwords = [line.strip() for line in open("data2/stopwords.txt","r",encoding="utf-8").readlines()]
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
preprosess_text(android_development, sentences, 'android_development')
preprosess_text(big_data, sentences, 'big_data')
preprosess_text(deep_learning, sentences, 'deep_learning')
preprosess_text(education, sentences, 'education')
preprosess_text(mechine_learning, sentences, 'mechine_learning')
preprosess_text(nature_language_process, sentences, 'nature_language_process')
preprosess_text(operate, sentences, 'operate')
preprosess_text(operation_maintenance, sentences, 'operation_maintenance')
preprosess_text(production_manager, sentences, 'production_manager')
preprosess_text(ui_design, sentences, 'ui_design')

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
        self.vectorize = CountVectorizer(analyzer='word',ngram_range=(1,10),max_features=45000)
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

#加载全部的数据，利用朴素贝叶斯网络进行分类
sql = "select * from all_job"
data = pda.read_sql(sql,conn1)
data1 = data.job_request.values.tolist()
data2 = data.values.tolist()
print(data2)
#对文本进行切词，并去除停用词
sentences = []
i = 0
for line in data1:
    try:
        print("正在处理第"+str(i+1)+"条工作数据..................")
        segs = jieba.lcut(line)
        segs = filter(lambda x:len(x)>1,segs)
        segs = filter(lambda x:x not in stopwords,segs)
        sentences.append((" ".join(segs)))
        i+=1
    except Exception:
        continue

for i in range(len(sentences)):
    print("第"+str(i+1)+"条工作记录数据.....................")
    print(sentences[i])
    result = text_classfiler.predict(sentences[i])
    print(result[0])

    if result == "android_development ":
            sql1 = "insert into android_development  VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][3])+"','"+str(data2[i][4])+"','"+str(data2[i][5])+"','"+str(data2[i][6])+"','"+str(data2[i][7])+"')"
            try:
                conn.query(sql1)
                conn.commit()
            except Exception:
                print("数据存储异常,请检查数据库..........."+traceback.format_exc())
                conn.rollback()

    elif result == "big_data":
            sql1 = "insert into big_data VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][3])+"','"+str(data2[i][4])+"','"+str(data2[i][5])+"','"+str(data2[i][6])+"','"+str(data2[i][7])+"')"
            try:
                conn.query(sql1)
                conn.commit()
            except Exception:
                print("数据存储异常,请检查数据库..........." + traceback.format_exc())
                conn.rollback()

    elif result == "deep_learning":
            sql1 = "insert into deep_learning VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][3])+"','"+str(data2[i][4])+"','"+str(data2[i][5])+"','"+str(data2[i][6])+"','"+str(data2[i][7])+"')"
            try:
                conn.query(sql1)
                conn.commit()
            except Exception:
                print("数据存储异常,请检查数据库..........." + traceback.format_exc())
                conn.rollback()

    elif result == "education":
            sql1 = "insert into education VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][3])+"','"+str(data2[i][4])+"','"+str(data2[i][5])+"','"+str(data2[i][6])+"','"+str(data2[i][7])+"')"
            try:
                conn.query(sql1)
                conn.commit()
            except Exception:
                print("数据存储异常,请检查数据库..........." + traceback.format_exc())
                conn.rollback()

    elif result == "mechine_learning":
            sql1 = "insert into mechine_learning VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][3])+"','"+str(data2[i][4])+"','"+str(data2[i][5])+"','"+str(data2[i][6])+"','"+str(data2[i][7])+"')"
            try:
                conn.query(sql1)
                conn.commit()
            except Exception:
                print("数据存储异常,请检查数据库..........." + traceback.format_exc())
                conn.rollback()

    elif result == "natural_language_processing":
            sql1 = "insert into natural_language_processing VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][7])+"')"
            try:
                conn.query(sql1)
                conn.commit()
            except Exception:
                print("数据存储异常,请检查数据库..........." + traceback.format_exc())
                conn.rollback()

    if result == "operate":
            sql1 = "insert into operate VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][3])+"','"+str(data2[i][4])+"','"+str(data2[i][5])+"','"+str(data2[i][6])+"','"+str(data2[i][7])+"')"
            try:
                conn.query(sql1)
                conn.commit()
            except Exception:
                print("数据存储异常,请检查数据库..........." + traceback.format_exc())
                conn.rollback()

    elif result == "operation_maintenance":
            sql1 = "insert into operation_maintenance VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][3])+"','"+str(data2[i][4])+"','"+str(data2[i][5])+"','"+str(data2[i][6])+"','"+str(data2[i][7])+"')"
            try:
                conn.query(sql1)
                conn.commit()
            except Exception:
                print("数据存储异常,请检查数据库..........." + traceback.format_exc())
                conn.rollback()

    elif result == "production_manager":
            sql1 = "insert into production_manager VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][3])+"','"+str(data2[i][4])+"','"+str(data2[i][5])+"','"+str(data2[i][6])+"','"+str(data2[i][7])+"')"
            conn.query(sql1)
            conn.commit()

    elif result == "ui_design":
            sql1 = "insert into ui_design VALUES ('"+str(data2[i][0])+"','"+str(data2[i][1])+"','"+str(data2[i][2])+"','"+str(data2[i][3])+"','"+str(data2[i][4])+"','"+str(data2[i][5])+"','"+str(data2[i][6])+"','"+str(data2[i][7])+"')"
            try:
                conn.query(sql1)
                conn.commit()
            except Exception:
                print("数据存储异常,请检查数据库..........." + traceback.format_exc())
                conn.rollback()

    print(text_classfiler.score(x_test,y_test))