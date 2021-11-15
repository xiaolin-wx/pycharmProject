from pymysql import Connect

# 设置数据库的连接
conn = Connect(host="localhost",user="root",password="13820541017",db="jobdata",port=3306,charset="utf8")
cursor = conn.cursor()

# table_list = ['algorithm_engineer','android_development','big_data','deep_learning','education','mechine_learning','nature_language_process','operate','operation_maintenance','production_manager','ui_design']
table_list = ['real_estate_sales']
for i in range(len(table_list)):
    # 从一个其他表中读取数据,然后将所有的数据全部放入all_job中
    sql = "select * from {};".format(table_list[i])
    cursor.execute(sql)
    result = cursor.fetchall()
    print(len(result))
    for item in result:
        try:
            print(item)
            if item[6]==None and item[7]==None:
                sql_ = "insert into all_job values ('"+item[0]+"','"+item[1]+"',NULL,'"+item[3]+"','"+item[4]+"','"+item[5]+"',NULL,NULL);"
                cursor.execute(sql_)
                conn.commit()
            else:
                sql_ = "insert into all_job values ('"+item[0]+"','"+item[1]+"','"+str(item[2])+"','"+item[3]+"','"+item[4]+"','"+item[5]+"','"+str(item[6])+"','"+str(item[7])+"');"
                cursor.execute(sql_)
                conn.commit()
        except:
            print("数据插入异常.............")
            conn.rollback()
