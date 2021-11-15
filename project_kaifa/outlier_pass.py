from pymysql import Connect

# 设置数据库的链接
conn = Connect(host="localhost",user="root",password="13820541017",db="job_category",charset="utf8")
cursor = conn.cursor()

# 分别设置三个列表用来存放一些列表名字和异常值
table_list = ['computer','education','electronics','finance','medical','real_estate','service','transportation']
min_salary = [1500,1500,1400,1300,1400,1400,1300,1300,1350]
max_salary = [29500,15000,21000,20000,21000,18000,17000,18000]

# 循环遍历所有的表，从表中去除异常值
for i in range(len(table_list)):
    sql = "select job_name,company_name,salary,address from {}".format(str(table_list[i]))
    cursor.execute(sql)
    result = cursor.fetchall()
    for item in result:
        if item[2] == None:
            pass
        elif item[2]>max_salary[i] or item[2]<min_salary[i]:
            print(item[2])
            sql1 = "update "+str(table_list[i])+" set salary=NULL where job_name='"+str(item[0])+"' and company_name='"+str(item[1])+"' and address='"+str(item[3])+"'"
            print(sql1)
            cursor.execute(sql1)
            conn.commit()
