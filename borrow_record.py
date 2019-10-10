# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\编程文件\数据库课设\borrow_record.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFrame,QHBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_Dialog9(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 555)
        palette1 = QtGui.QPalette()
        palette1.setColor(QtGui.QPalette.Background, QtGui.QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("./background/2.jpg").scaled(Dialog.size())))  # 设置背景图片
        Dialog.setPalette(palette1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(480,20,93,28))
        # self.textEdit = QtWidgets.QTextEdit(Dialog)
        # self.textEdit.setGeometry(QtCore.QRect(10, 60, 621, 481))
        # self.textEdit.setObjectName("textEdit")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 20, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setGeometry(QtCore.QRect(10,60,621,481))
        self.tableWidget.setHorizontalHeaderLabels(["索书号","书名","作者","借阅时间","归还日期"])
        self.tableWidget.setObjectName("tableWidget")
        self.frame = QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10,60,621,481))
        self.frame.setVisible(False)
        self.hboxLayout = QHBoxLayout(self.frame)
        self.myHtml = QWebEngineView()
        self.myHtml.load(QUrl("file:///D:/编程文件/数据库课设/pie.html"))
        self.hboxLayout.addWidget(self.myHtml)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "借阅历史"))
        self.comboBox.setItemText(0, _translate("Dialog", "借阅历史"))
        self.comboBox.setItemText(1, _translate("Dialog", "可视化分析"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "类别可视化"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "日期可视化"))
        self.pushButton.setText(_translate("Dialog", "返回"))

