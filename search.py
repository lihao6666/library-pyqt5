# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\编程文件\数据库课设\search.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 329)
        palette1 = QtGui.QPalette()
        palette1.setColor(QtGui.QPalette.Background, QtGui.QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("./background/2.jpg").scaled(Dialog.size())))  # 设置背景图片
        Dialog.setPalette(palette1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 20, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 20, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 73, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setGeometry(QtCore.QRect(20,60,521,261))
        self.tableWidget.setHorizontalHeaderLabels(["书名","作者","索书号","出版社","可借","馆藏","事件"])
        self.tableWidget.setObjectName("tableWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "查询"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "请输入你想查询的书籍"))
        self.pushButton.setText(_translate("Dialog", "搜索"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.comboBox.setItemText(0, _translate("Dialog", "书名"))
        self.comboBox.setItemText(1, _translate("Dialog", "类别"))

