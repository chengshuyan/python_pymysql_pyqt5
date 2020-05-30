from PyQt5 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget();
window.show()
sys.exit(app.exec_())

db = pymysql.connect(host='localhost', user='root', password='666666', port=3306, db='SQLB17121207', charset='utf8')
# 开启mysql的游标功能，创建一个游标对象；
cursor = db.cursor()
# 要执行的SQL语句；
sql_create_table = '''
 CREATE TABLE F_S(
 航班号 CHAR(8) PRIMARY KEY NOT NULL,
 起点 VARCHAR(15),
 终点 VARCHAR(15),
 日期 DATETIME(6) NOT NULL,
 起飞时刻 CHAR(6),
 到达时刻 CHAR(6),
 剩余座位数 INT(4),
 票价 FLOAT(8),
 折扣票价 FLOAT(8),
 折扣率 FLOAT(8),
 航班所属航班公司 VARCHAR(20)
);'''
sql = """
     SHOW TABLES
"""
# 使用游标对象执行SQL语句；
cursor.execute(sql)
# 使用fetchone()方法，获取返回的结果，但是需要用变量保存返回结果；
data = cursor.fetchall()
print(data)
# 断开数据库的连接，释放资源；
db.close()