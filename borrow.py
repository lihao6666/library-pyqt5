# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\编程文件\数据库课设\borrow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog6(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 329)
        palette1 = QtGui.QPalette()
        palette1.setColor(QtGui.QPalette.Background, QtGui.QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("./background/2.jpg").scaled(Dialog.size())))  # 设置背景图片
        Dialog.setPalette(palette1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 211, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setGeometry(QtCore.QRect(20,60,521,261))
        self.tableWidget.setHorizontalHeaderLabels(["索书号","书名","作者","借阅时间","截止日期","事件"])
        self.tableWidget.setObjectName("tableWidget")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "借阅详情"))
        self.label.setText(_translate("Dialog", "您的当前借阅详情："))
        self.pushButton.setText(_translate("Dialog", "退出"))

