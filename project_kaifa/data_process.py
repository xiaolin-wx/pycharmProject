from pymysql import Connect

# 设置数据库的连接
conn = Connect(host="localhost",user="root",password="13820541017",db="job_list1",port=3306,charset="utf8")
cursor=conn.cursor()

table_list = ["nature_language","deep_learning","computer_vision","big_data","machine_learning","production_manager","education","finance","service","transportation"]
# for i in range(len(table_list)):
#     print("正在处理表 "+table_list[i]+" 的数据")
#     # 从数据库中取出数据
#     sql = "select job_name,company_name,salary,job_address from {}".format(str(table_list[i]))
#     print(sql)
#     cursor.execute(sql)
#     result = cursor.fetchall()
#
#     for item in result:
#         try:
#             salary = str(item[2])
#             print(salary)
#             # 将没有工资数据的salary置为空,后续使用插值法来解决
#             if salary == "":
#                 sql_1 = "update "+table_list[i]+" set salary=NULL where salary=''".format(str(table_list[i]))
#                 print(sql_1)
#                 cursor.execute(sql_1)
#                 conn.commit()
#
#             # 处理以"元/天"结尾的工资分离
#             if salary[-3:] == "元/天":
#                 min_max_salary = int(float(str(salary).replace("元/天", "")) * 30)
#                 sql_1 = "update "+table_list[i]+" set min_salary='"+str(min_max_salary)+"',max_salary='"+str(min_max_salary)+"' where job_name='"+str(item[0])+"' and company_name='"+str(item[1])+"' and job_address='"+str(item[3])+"' and salary regexp '元/天$'"
#                 cursor.execute(sql_1)
#                 conn.commit()
#
#             # 处理以“万/年”结束的工资分离
#             if salary[-3:] == "万/年":
#                 min_salary,max_salary = salary.split("-")
#                 min_salary = int(float(min_salary)*10000/12)
#                 max_salary = int(float(str(max_salary).replace("万/年",""))*10000/12)
#                 sql_1 = "update "+table_list[i]+" set min_salary='"+str(min_salary)+"',max_salary='"+str(max_salary)+"' where job_name='"+str(item[0])+"' and company_name='"+str(item[1])+"' and job_address='"+str(item[3])+"' and salary regexp '万/年$'"
#                 cursor.execute(sql_1)
#                 conn.commit()
#
#             # 处理以“千/月”结束的工资分离
#             if salary[-3:] == "千/月":
#                 min_salary, max_salary = salary.split("-")
#                 min_salary = int(float(min_salary) * 1000)
#                 max_salary = int(float(str(max_salary).replace("千/月", "")) * 1000)
#                 sql_1 = "update "+table_list[i]+" set min_salary='" + str(min_salary) + "',max_salary='" + str(max_salary) + "' where job_name='" + str(item[0]) + "' and company_name='" + str(item[1]) + "' and job_address='" + str(item[3]) + "' and salary regexp '千/月$'"
#                 cursor.execute(sql_1)
#                 conn.commit()
#
#             # 处理以“万/年”结束的工资分离
#             if salary[-3:] == "万/月":
#                 min_salary, max_salary = salary.split("-")
#                 min_salary = int(float(min_salary) * 10000)
#                 max_salary = int(float(str(max_salary).replace("万/月", "")) * 10000)
#                 sql_1 = "update "+table_list[i]+" set min_salary='"+str(min_salary)+"',max_salary='"+str(max_salary)+"' where job_name='"+str(item[0])+"' and company_name='"+str(item[1])+ "' and job_address='" + str(item[3]) + "' and salary regexp '万/月$'"
#                 print(sql_1)
#                 cursor.execute(sql_1)
#                 conn.commit()
#         except:
#             print("数据字段处理错误")
#             continue

for i in range(len(table_list)):
    print("******************************"+str(table_list[i])+"****************************")
    sql_2 = "update "+str(table_list[i])+" set salary=(min_salary+max_salary)/2"
    cursor.execute(sql_2)
    conn.commit()
