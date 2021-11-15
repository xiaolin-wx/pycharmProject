import pandas as pda
from pymysql import Connect
import warnings
from scipy.interpolate import lagrange      #导入拉格朗日插值函数
warnings.filterwarnings("ignore")     # 设置忽略警告信息

# 设置数据库的链接
conn = Connect(host="localhost",user="root",password="13820541017",db="job_category",charset="utf8")
cursor = conn.cursor()
table_list = ["computer","education","electronics","finance","medical","real_estate","service","transportation",]
education_requirement = ["硕士","本科","大专"]
address_list = ["北京","上海","广州","深圳","杭州","武汉","成都","重庆","西安"]
# 循环遍历一个列表，运行程序之前首先创建一个data_processed文件夹，然后将处理好的文件都放入此文件夹当中
for k1 in range(len(table_list)):
    for k2 in range(len(address_list)):
        print("========================>"+table_list[k1]+address_list[k2]+".xlsx <================================")
        # 定义输出文件的路径
        outputfile = "data_address_processed/"+table_list[k1]+address_list[k2]+".xlsx"
        # 依次读取每个表中的数据
        data = pda.read_excel("data_address/"+table_list[k1]+address_list[k2]+".xlsx")

        # 过滤异常值
        # data2[u'salary'][(data2[u'salary']<max_salary[k1])|(data2[u'salary']>min_salary[k1])] = None

        # 构建拉格朗日函数，使他能够进行正确的插值
        def ployinterp_column(s,n,k=1):
            y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]
            y=y[y.notnull()]
            return int(abs(lagrange(y.index,list(y))(n)))
        k=0

        # 依次遍历excel表格中的每一行数据
        for i in data.columns:
            for j in range(len(data)):
                # 如果遇到salary的值为空，就进行插值
                if (data[i].isnull())[j]:
                    # print(data2[i])
                    data[i][j] = ployinterp_column(data[i],j)
                    print(data[i][j])
                    k+=1

        # 最后将插值的结果存放到指定的文件夹中
        data.to_excel(outputfile)
        print("总处理了"+str(k)+"条缺失值.............................")

# 将学历要求为硕士、本科、专科的全部查找出来并写入到excel表格中
# for i in range(len(table_list)):
#     print("========================== "+table_list[i]+" ==============================")
#     for j in range(len(address_list)):
#
#         # 使用Python正则表达式，将数据库中北京的数据都提取出来，然后写入excel表格中
#         sql = "select job_name,company_name,salary,address from "+str(table_list[i])+" where address regexp '"+str(address_list[j])+"'"
#         print(sql)
#         data = pda.read_sql(sql,conn)
#         file_name = table_list[i]+address_list[j]+".xlsx"
#         data.to_excel("data_address/"+file_name)

# 将salary设置为最大工资与最小工资的平均值
# for i in range(len(table_list)):
#     print("============================="+str(table_list[i])+"================================")
#     sql_2 = "update "+str(table_list[i])+" set salary=(min_salary+max_salary)/2"
#     cursor.execute(sql_2)
#     conn.commit()