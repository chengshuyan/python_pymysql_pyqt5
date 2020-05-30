# 导包
import pymysql
# 使用pymysql连接上mysql数据库服务器，创建了一个数据库对象；
db = pymysql.connect(host='localhost',user='root', password='666666',
     port=3306, db='SQLB17121207', charset='utf8')
# 开启mysql的游标功能，创建一个游标对象；
cursor = db.cursor()
# 要执行的SQL语句；
sql = "select * from S"
# 使用游标对象执行SQL语句；
cursor.execute(sql)
# 使用fetchone()方法，获取返回的结果，但是需要用变量保存返回结果；
data = cursor.fetchone()
print(data)
data = cursor.fetchall()
for a,b,c,d in data:
     print(a,b,c,d);
# 断开数据库的连接，释放资源；
db.close()