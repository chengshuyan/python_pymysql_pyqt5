# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import op

UserName = 'root'
PassWord = '666666'
class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.UserName = UserName
        self.PassWord = PassWord
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 409)
        Form.setAutoFillBackground(False)
        self.form = Form
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 60, 111, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 250, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 180, 30, 29))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(250, 130, 148, 21))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 130, 51, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 190, 148, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请输入用户信息"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.label_3.setText(_translate("Form", "密码"))
        self.label_2.setText(_translate("Form", "用户名"))
        self.pushButton.clicked.connect(self.Login)

    def jump_to_main(self):
        self.dialog.close()

    def Login(self):
        if(self.lineEdit.text() == self.UserName and self.lineEdit_2.text() == self.PassWord):
            print("登陆成功！")
            self.form.close()
            form1 = QtWidgets.QDialog()
            ui = op.Ui_Form()
            ui.setupUi(form1)
            form1.show()
            form1.exec_()
        elif(self.lineEdit.text() != self.UserName):
            print("用户名错误!")
        elif(self.lineEdit_2.text() == self.PassWord):
            print("密码错误!")