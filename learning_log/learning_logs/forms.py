from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):   #定义了一个类
    class Meta:   #内嵌了一个类
        model = Topic #根据Topic创建一个表单
        fields = ['text']   #表单只包含字段text
        labels = {'text':''}  #Django不要为字段text生成标签