# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'op1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import Dialog

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 359)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 230, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(51, 255, 81, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 230, 71, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 260, 21, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(320, 260, 20, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(420, 260, 31, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 300, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonclicked)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 260, 71, 21))
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setMaxVisibleItems(3030)
        self.comboBox_2.setMaxCount(3030)
        self.comboBox_2.setMinimumContentsLength(1991)
        self.comboBox_2.setObjectName("comboBox_2")
        years = [" 2000 ", " 2001 ", " 2002 ", " 2003 ", " 2004 ", " 2005 ", " 2006 ", " 2007 ", " 2008 ", " 2009 ",
                 " 2010 ", " 2011 ", " 2012 ", " 2013 ", " 2014 ", " 2015 ", " 2016 ", " 2017 ", " 2018 ", " 2019 ",
                 "2020"]
        self.comboBox_2.addItems(years)
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(240, 260, 71, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(
            [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 ", " 11 ", " 12 "])
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(340, 260, 71, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItems(
            [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 ", " 11 ", " 12 ", " 13 ", " 14 ",
             " 15 ", " 16 ", " 17 ", " 18 ", " 19 ", " 20 ", " 21 ", " 22 ", " 23 ", " 24 ", " 25 ", " 26 ", " 27 ",
             " 28 ", " 29 ", " 30 ", " 31 "])
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(30, 40, 501, 181))
        self.tableView.setObjectName("tableView")
        self.tableView.setWindowTitle("航班信息表")
        self.model = QtGui.QStandardItemModel(40,11)
        self.model.setHorizontalHeaderLabels(['航班号', '起点', '终点', '日期','起飞时刻','到达时刻','剩余座位数','票价','折扣票价','折扣率','航班所属航班公司'])
        #********获得数据
        self.tableView.setModel(self.model)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "航班号"))
        self.label_2.setText(_translate("Form", "日期"))
        self.label_3.setText(_translate("Form", "年"))
        self.label_4.setText(_translate("Form", "月"))
        self.label_5.setText(_translate("Form", "日"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "退出"))

    def buttonclicked(self):
        #从lineEdit、combobox_2\combobox_3\combobox_4获得数据
        number = self.lineEdit.text()
        year = self.comboBox_2.currentText()
        month = self.comboBox_3.currentText()
        date = self.comboBox_4.currentText()
        '''
        print('year = ',year,len(year),year[2:4],'/')
        print('month = ',month,len(month),'/')
        print('date = ',date,len(date),'/')
        '''
        if int(month) < 10:
            month = '0'+month[1:]
        if int(date) < 10:
            date = '0'+date[1:]
        print(month)
        print(date)
        if int(month) < 10:
            dataTime = year[3:5] + month[:2] + date[:2] + '000000'
        else:
            dataTime = year[3:5] + month[1:3] + date[1:3] + '000000'
        #dataTime1 = '140505050505'
        print(dataTime)
        #根据数据对票务查询
        # 使用游标对象执行SQL语句；
        sql1 = '''SELECT * FROM F_S WHERE 航班号 = \'''' +number+ '''\' AND 日期 = \'''' + dataTime + '\''
        sql = "SELECT * FROM F_S"
        sql2 = '''SELECT * FROM F_S WHERE 航班号 = \'''' + number + '''\' '''
        print(Dialog.UserName)
        print(Dialog.PassWord)
        db = pymysql.connect(host='localhost', user=Dialog.UserName, password=Dialog.PassWord, port=3306, db='SQLB17121207',
                             charset='utf8')
        # 开启mysql的游标功能，创建一个游标对象；
        cursor = db.cursor()
        print(sql1)
        cursor.execute(sql1)
        # 使用fetchone()方法，获取返回的结果，但是需要用变量保存返回结果；
        data = cursor.fetchall()
        print(data)
        db.close()
        #list = (('K0001', '河北', '山西', 14050505, '0911', '1022', 999, 998.0, 333.0, 0.7, 'SH48A'), ('Y7381', '河北', '山西', 14050505, '1933', '1022', 999, 132.0, 333.0, 0.8, 'SH48A'), ('Z1919', '湖南', '山东', 14050505, '1933', '2235', 676, 132.0, 67.0, 0.8, 'JNSS'))
        # 断开数据库的连接，释放资源；
        r = 0
        c = 0
        for row in data:
            c = 0
            for column in row:
                if c == 3 or c > 5 and c < 10:
                    item = QtGui.QStandardItem(str(column))
                else:
                    item = QtGui.QStandardItem(column)
                # 设置每个位置的文本值
                self.model.setItem(r, c, item)
                c = c + 1
            r = r + 1