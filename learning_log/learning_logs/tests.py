from django.test import TestCase

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")
django.setup()
# Create your tests here.

from learning_logs.models import Topic

def test():
    '''显示所有主题'''
    topics = Topic.objects.order_by('date_added')  #查询数据库，请求提供Topics对象，并按照属性date_added对他们进行排序
    context = {'topic': topics}    #定义一个将要发送给模板的上下文
    for entity in topics:
        print(entity)
test()