# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import Dialog
import op1

class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(561, 396)
        self.form = Form
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 90, 161, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 250, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "欢迎使用票务管理系统"))
        self.pushButton.setText(_translate("Form", "票务管理"))
        self.pushButton_2.setText(_translate("Form", "票务查询"))
        self.pushButton.clicked.connect(self.jump_to_log)
        self.pushButton_2.clicked.connect(self.jump_to_op)

    def jump_to_log(self):
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = Dialog.Ui_Form()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.form.show()

    def jump_to_op(self):
        self.form.hide()
        form2 = QtWidgets.QDialog()
        ui = op1.Ui_Form()
        ui.setupUi(form2)
        form2.show()
        form2.exec_()
        self.form.show()