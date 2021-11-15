from django.shortcuts import render,redirect
from pymysql import Connect
from django.template import RequestContext
from stuMng import models
#数据库的链接
conn = Connect(host="localhost", user="root", password="linwenxin", port=3306, db="db_sms", charset='utf8')
#创建游标
cursor = conn.cursor()

# Create your views here.
def login(request):
    # 如果以get方式请求，返回前端界面
    if request.method == "GET":
        return render(request, 'login.html')
    # 如果请求方式为post，则接受前台的数据
    if request.method == "POST" and 'submit' in request.POST:
        # 获取数据库中的内容
        cursor.execute("select username,password from tb_admin")
        result = cursor.fetchall()
        login_name = result[0][0]
        login_pass = result[0][1]
        usename = request.POST.get('username')
        password = request.POST.get('password')
        if usename == login_name and password == login_pass:
            return redirect("/stuMng/stuMngload/")
        # 如果用户名和密码没有输入，提示错误信息
        elif usename == "" or password == "":
            msg = "请输入用户名或密码"
            return render(request,"login.html", {'msg': msg})
        elif usename != login_name or password != login_pass:
            msg = "密码或账号有误！ 请重新输入"
            return render(request,"login.html", {'msg': msg})
    return render(request, 'login.html')

def stuMngload(request):
    return render(request,"stuMngload.html")


def class_load(request):
    return render(request,"class_load.html")

#添加班级
def add_class(request):
    if request.method == 'POST':
        #获取表单的数据
        #class_id = request.POST.get("classid")
        class_name = request.POST.get("classname")
        #保存到数据库
       # models.TbClass.objects.create(name=class_name, isdele=0)
        user = models.TbClass(name=class_name, isdele=0)
        user.save()
        return redirect("/stuMng/check_class/")
    return render(request, 'add_class.html')

#修改班级
def edit_class(request):
    if request.method == "POST":
        #获取表单信息
        id = request.POST.get("classid")
        name = request.POST.get("classname")
        #根据id查找
        class_id = models.TbClass.objects.get(id=id)
        #修改
        class_id.name = name
        class_id.save()
        #重定向到班级列表
        return redirect("/stuMng/check_class")
    else:
        #获取id
        id = request.GET.get('id')
        dict = {"id": None, "name": None}
        # 去数据库中查找相应数据
        class_id = models.TbClass.objects.get(id=id)
        class_list = models.TbClass.objects.all()
        for item in class_list:
            if str(item.id) == str(id):
                dict["id"] = item.id
                dict["name"] = item.name
        return render(request, "edit_class.html", {'class_id': class_id, "class_list": dict})

#删除班级
def delete_class(request):
    #获取删除id
    id = request.GET.get("id")
    print(id)
    #根据id删除
    models.TbClass.objects.filter(id=id).delete()
    return redirect("/stuMng/check_class")

#查看班级
def check_class(request):
    class_list = models.TbClass.objects.all()
    return render(request, 'check_class.html', {"class_list": class_list})

def stu_load(request):
    return render(request, "stu_load.html")

#搜索信息--班级
def search_class(request):
    # 获取id
    name = request.POST.get('classname')
    print(name)
    dict = {"id": None, "name": None}
    # 去数据库中查找相应数据
    # class_name = models.TbClass.objects.filter(name=name)
    class_list = models.TbClass.objects.all()
    for item in class_list:
        if str(item.name) == str(name):
            dict["id"] = item.id
            dict["name"] = item.name
            print(item.id)
            print(item.name)
    return render(request, "search_class.html", {"class_list": dict})

#添加学生
def add_stu(request):
    if request.method == 'POST':
        stu_name = request.POST.get("stuname")
        stu_sex = request.POST.get("stusex")
        stu_class = request.POST.get("stuclass")
        stu_study = request.POST.get("stustudy")
        stu_tel = request.POST.get("stutel")
        user = models.TbStudent(name=stu_name,sex=stu_sex,class_id=stu_class,p_id=stu_study,tel=stu_tel ,isdele=0)
        user.save()
        return redirect("/stuMng/check_stu")
    return render(request, 'add_stu.html')

def check_stu(request):
    stu_list = models.TbStudent.objects.all()
    return render(request, 'check_stu.html',{'stu_list':stu_list})

#修改学生
def edit_stu(request):
    if request.method == "POST":
        #获取表单信息
        id = request.POST.get("stuid")
        name = request.POST.get("stuname")
        sex = request.POST.get("stusex")
        class_id = request.POST.get("stuclass")
        study = request.POST.get("stustudy")
        tel = request.POST.get("stutel")
        #根据id查找
        stu_id = models.TbStudent.objects.get(id=id)
        #修改
        stu_id.name = name
        stu_id.sex = sex
        stu_id.class_id = class_id
        stu_id.p_id = study
        stu_id.tel = tel
        stu_id.save()
        #重定向到班级列表
        return redirect("/stuMng/check_stu")
    else:
        # 获取id
        id = request.GET.get('id')

        dict = {"id": None, "name": None, "sex": None, "class_id": None, "p_id": None, "tel": None}
        # 去数据库中查找相应数据
        stu_id = models.TbStudent.objects.get(id=id)
        stu_list = models.TbStudent.objects.all()
        for item in stu_list:
            if str(item.id) == str(id):
                dict["id"] = item.id
                dict["name"] = item.name
                dict["sex"] = item.sex
                dict["class_id"] = item.class_id
                dict["p_id"] = item.p_id
                dict["tel"] = item.tel
        return render(request, "edit_stu.html", {'stu_id': stu_id, "stu_list": dict})

#删除学生
def delete_stu(request):
    # 获取删除id
    id = request.GET.get("id")
    print(id)
    # 根据id删除
    models.TbStudent.objects.filter(id=id).delete()
    return redirect("/stuMng/check_stu")

#搜索信息--学生
def search_stu(request):
    # 获取id
    name = request.POST.get('stuname')
    dict = {"id": None, "name": None}
    # 去数据库中查找相应数据
    stu_list = models.TbStudent.objects.all()
    for item in stu_list:
        if str(item.name) == str(name):
            dict["id"] = item.id
            dict["name"] = item.name
            dict["sex"] = item.sex
            dict["class_id"] = item.class_id
            dict["p_id"] = item.p_id
            dict["tel"] = item.tel
    return render(request, "search_stu.html", {"stu_list": dict})