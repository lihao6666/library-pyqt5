# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\编程文件\数据库课设\info.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog7(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(546, 329)
        palette1 = QtGui.QPalette()
        palette1.setColor(QtGui.QPalette.Background, QtGui.QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("./background/2.jpg").scaled(Dialog.size())))  # 设置背景图片
        Dialog.setPalette(palette1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 211, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 521, 241))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 10, 93, 28))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "账号信息"))
        self.label.setText(_translate("Dialog", "您的账号信息："))
        self.pushButton.setText(_translate("Dialog", "返回"))
        self.comboBox.setItemText(0, _translate("Dialog", "读者信息"))
        self.comboBox.setItemText(1, _translate("Dialog", "借阅证信息"))
        self.pushButton_2.setText(_translate("Dialog", "充值"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "请输入金额"))

