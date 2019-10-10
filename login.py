# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\编程文件\数据库课设\login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 329)
        # MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        palette1 = QtGui.QPalette()
        palette1.setColor(QtGui.QPalette.Background, QtGui.QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("./background/start.jpg").scaled(MainWindow.size())))  # 设置背景图片
        MainWindow.setPalette(palette1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 80, 251, 31))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 130, 251, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 80, 71, 31))
        self.label.setStyleSheet("color: rgb(85, 170, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 71, 31))
        self.label_3.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 190, 131, 41))
        self.pushButton.setStyleSheet("font: 9pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(137, 184, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 40, 71, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(137, 184, 255);\n"
"font: 9pt \"黑体\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(100, 220, 115, 19))
        self.radioButton.setStyleSheet("color: rgb(85, 170, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 190, 115, 19))
        self.radioButton_2.setStyleSheet("color: rgb(85, 170, 255);")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登录"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入学号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label.setText(_translate("MainWindow", "学号："))
        self.label_3.setText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_3.setText(_translate("MainWindow", "注册"))
        self.radioButton.setText(_translate("MainWindow", "管理员"))
        self.radioButton_2.setText(_translate("MainWindow", "学生"))