'''定义learning_logs的URL模式'''

from django.conf.urls import url  #导入函数url，需要使用他来将URL映射到视图
from . import views   #导入views

urlpatterns = [    #列表，包含可在应用程序learning_logs中请求的网页
    #主页
    url(r'^$' , views.index, name='index'),  #正则表达式 + 指定要调用的试图函数 + 将urls模式的名称指定为index
    url(r'^topics/$',views.topics,name='topics'), #由于主页URL的正则表达式中添加了topics 单词topics后面不能有单词
    url(r'^new_topic/$',views.new_topic,name='new_topic'),  #将请求交给视图函数new_topic
]

app_name='learning_logs'