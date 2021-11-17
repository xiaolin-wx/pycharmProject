import pymysql

db = pymysql.connect(host="localhost",  # 连接到数据库，服务器为本机
                     user="root",  # 用户名
                     passwd="linwenxin",  # 密码
                     db="streetlight")  # 数据库名
cursor = db.cursor()  # 获得数据库游标
SQL = """CREATE TABLE `light` (
  `id`  int NOT NULL auto_increment,
  `address` varchar(100)DEFAULT NULL,
  `jingdu` varchar(100) DEFAULT NULL,
  `weidu` varchar(100) DEFAULT NULL,
  `datetime` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
)auto_increment=1;
"""
#id->路灯编号
#address->路灯地址
#coordinate->路灯的坐标
#datetime->时间
#state->状态
 # 创建新的数据表
cursor.execute(SQL)

db.close()
 # 关闭数据库连接