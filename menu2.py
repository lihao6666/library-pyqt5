# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\编程文件\数据库课设\menu2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 329)
        palette1 = QtGui.QPalette()
        palette1.setColor(QtGui.QPalette.Background, QtGui.QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("./background/2.jpg").scaled(Dialog.size())))  # 设置背景图片
        Dialog.setPalette(palette1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 230, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 130, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 80, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 180, 141, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "账号信息"))
        self.pushButton_2.setText(_translate("Dialog", "当前借阅"))
        self.label.setText(_translate("Dialog", "      合肥工业大学图书馆(学生）"))
        self.pushButton.setText(_translate("Dialog", "图书查询"))
        self.pushButton_4.setText(_translate("Dialog", "借阅历史"))

