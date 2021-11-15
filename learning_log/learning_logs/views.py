from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm
# Create your views here.
def index(request):
    '''学习笔记的主页'''
    return render(request,'index.html')

def topics(request):    #从服务器接收到对象
    '''显示所有主题'''
    topics = Topic.objects.order_by('date_added')  #查询数据库，请求提供Topics对象，并按照属性date_added对他们进行排序
    context = {'topics': topics}    #定义一个将要发送给模板的上下文 json==dirct
    return render(request,'topics.html',context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据：创建一个新表单
        form = TopicForm
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'new_topic.html', context)