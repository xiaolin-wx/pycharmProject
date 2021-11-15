"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#导入了为项目和管理网站管理URL的函数模块
from django.conf.urls import include,url
from django.contrib import  admin

urlpatterns = [    #文件主体定义了变量urlpatterns
   # url('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),    #定义了可在管理网站中请求的所有URL
    url(r'',include('learning_logs.urls')),   #让我们能够将learning_logs的URL同项目中的其他URL区分开
    #对项目开始扩展是很有帮助
]
