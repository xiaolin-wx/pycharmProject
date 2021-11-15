from django.db import models

# Create your models here.
class Topic(models.Model):    #继承了Model——Django中定义了模型基本功能的类
    '''用户学习的主题'''
    text = models.CharField(max_length=200)    #属性text是一个CharField——由字符或文本组成的数据
    date_added = models.DateTimeField(auto_now_add=True)    #属性date_added是一个DateTimeField——记录日期和时间的数据

    def __str__(self):    #显示模型的简单表示
        '''返回模型的字符串表示'''
        return self.text

class Entry(models.Model):   #Entry也进行了继承
    '''学到的有关某个主题的具体知识'''
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)   #第一个属性Topic是一个ForeignKey（外键）实例
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:   #在Entry类中嵌套了Meta类
        verbose_name_plural = 'entries'

    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text[:50] + "..."   #只显示前50个字符   省略号指出显示的并非整个条目