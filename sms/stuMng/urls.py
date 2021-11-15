from django.urls import path
from stuMng import views

app_name = 'stuMng'

urlpatterns = [
    path("login/", views.login,name='login'),
    path("stuMngload/", views.stuMngload, name='stuMngload'),
    path("class_load/", views.class_load, name= 'class_load'),
    path("add_class/", views.add_class, name='add_class'),
    path("check_class/", views.check_class, name='check_class'),
    path("edit_class/", views.edit_class, name='edit_class'),
    path("delete_class/", views.delete_class, name='delete_class'),
    path("search_class/", views.search_class, name='search_class'),
    path("add_stu/", views.add_stu, name='add_stu'),
    path("check_stu/", views.check_stu, name='check_stu'),
    path("stu_load/", views.stu_load, name='stu_load'),
    path("edit_stu/", views.edit_stu, name='edit_stu'),
    path("delete_stu/", views.delete_stu, name='delete_stu'),
    path("search_stu/", views.search_stu, name='search_stu'),
]