# 导包
import pymysql
from PyQt5.QtWidgets import QApplication,QMainWindow

import sys
# 使用pymysql连接上mysql数据库服务器，创建了一个数据库对象；

if __name__ == '__main__':
     app = QApplication(sys.argv)
     sys.exit(app.exec_())