# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\编程文件\数据库课设\add_book.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 329)
        palette1 = QtGui.QPalette()
        palette1.setColor(QtGui.QPalette.Background, QtGui.QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("./background/start.jpg").scaled(Dialog.size())))  # 设置背景图片
        Dialog.setPalette(palette1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 200, 121, 31))
        self.pushButton.setStyleSheet("background-color: rgb(137, 184, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(60, 140, 171, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 61, 51))
        self.label_5.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 30, 171, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 61, 51))
        self.label_6.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 30, 171, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(290, 20, 61, 51))
        self.label_7.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(60, 80, 171, 31))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 61, 51))
        self.label_8.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(350, 140, 171, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(290, 130, 61, 51))
        self.label_9.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 200, 121, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(137, 184, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(350, 80, 171, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(290, 70, 61, 51))
        self.label_10.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加图书"))
        self.pushButton.setText(_translate("Dialog", "添加图书"))
        self.label_5.setText(_translate("Dialog", "数量："))
        self.label_6.setText(_translate("Dialog", "书名："))
        self.label_7.setText(_translate("Dialog", "作者："))
        self.label_8.setText(_translate("Dialog", "索书号："))
        self.label_9.setText(_translate("Dialog", "出版社："))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.label_10.setText(_translate("Dialog", "版本号："))

