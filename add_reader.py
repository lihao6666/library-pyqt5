# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\编程文件\数据库课设\add_reader.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog8(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 329)
        palette1 = QtGui.QPalette()
        palette1.setColor(QtGui.QPalette.Background, QtGui.QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("./background/2.jpg").scaled(Dialog.size())))  # 设置背景图片
        Dialog.setPalette(palette1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 61, 51))
        self.label_6.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 30, 171, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(290, 20, 61, 51))
        self.label_7.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(340, 30, 171, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 61, 51))
        self.label_8.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 80, 171, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(290, 70, 61, 51))
        self.label_9.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 80, 171, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 190, 121, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(137, 184, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 190, 121, 31))
        self.pushButton.setStyleSheet("background-color: rgb(137, 184, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加读者"))
        self.label_6.setText(_translate("Dialog", "学号："))
        self.label_7.setText(_translate("Dialog", "姓名："))
        self.label_8.setText(_translate("Dialog", "电话："))
        self.label_9.setText(_translate("Dialog", "借书卡："))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.pushButton.setText(_translate("Dialog", "添加借书卡"))

