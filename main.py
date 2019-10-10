import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QMessageBox,QHBoxLayout,QFrame
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QRect
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
from start import Ui_start
from login import Ui_MainWindow
from menu2 import Ui_Dialog2
from menu1 import Ui_Dialog
from add_book import Ui_Dialog3
from search import Ui_Dialog4
from card_id import Ui_Dialog5
from borrow import Ui_Dialog6
from info import Ui_Dialog7
from add_reader import Ui_Dialog8
from borrow_record import Ui_Dialog9
from mysql import mydb
from datetime import datetime
from PyQt5 import sip
from pie import BingTu
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

db = mydb()
db.lib_id = "123123"


class MyStart(QWidget, Ui_start):
    def __init__(self, parent=None):
        super(MyStart, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer(self)
        # 定义时间超时连接start_app
        self.timer.timeout.connect(self.go)
        # 定义时间任务是一次性任务
        self.timer.setSingleShot(True)
        # 启动时间任务
        self.timer.start(3000)

    def go(self):
        # time.sleep(5)
        self.timer.stop()
        self.close()
        self.mylogin = MyLogin()
        self.mylogin.show()


class MyLogin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyLogin, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.register)

    def login(self):
        stu_no = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        if len(stu_no) == 10:
            if self.radioButton_2.isChecked():
                if db.login(stu_no, passwd, 0) == True:
                    self.close()
                    self.stu_menu = Stu_Menu()
                    self.stu_menu.show()
                else:
                    button = QMessageBox.warning(self, "失败", "是否重新登录",
                                                 QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
                    if button == QMessageBox.Ok:
                        self.lineEdit_2.setText("")
                        self.lineEdit.setText("")

                    else:
                        self.close()
            else:
                if db.login(stu_no, passwd, 1) == True:
                    self.close()
                    self.manager_menu = Manager_Menu()
                    self.manager_menu.show()
                else:
                    button = QMessageBox.warning(self, "失败", "是否重新登录",
                                                 QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
                    if button == QMessageBox.Ok:
                        self.lineEdit_2.setText("")
                        self.lineEdit.setText("")

                    else:
                        self.close()
        else:
            button = QMessageBox.about(self, "失败", "学号错误")

    def register(self):
        stu_no = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        if len(stu_no) == 10:
            if self.radioButton_2.isChecked():
                if db.register(stu_no, passwd, 0) == True:
                    button = QMessageBox.about(self, "成功", "进入登录界面")
                else:
                    button = QMessageBox.warning(self, "失败", "是否重新注册",
                                                 QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
                    if button == QMessageBox.Ok:
                        self.lineEdit_2.setText("")
                        self.lineEdit.setText("")
                    else:
                        self.close()
            else:
                if db.register(stu_no, passwd, 1) == True:
                    button = QMessageBox.about(self, "成功", "进入登录界面")
                else:
                    button = QMessageBox.warning(self, "失败", "是否重新注册",
                                                 QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
                    if button == QMessageBox.Ok:
                        self.lineEdit_2.setText("")
                        self.lineEdit.setText("")
                    else:
                        self.close()
        else:
            button = QMessageBox.about(self, "失败", "学号错误")


class Manager_Menu(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super(Manager_Menu, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.borrow)
        self.pushButton_4.clicked.connect(self.reader)
        self.pushButton_5.clicked.connect(self.beifeng)
        self.pushButton_6.clicked.connect(self.huifu)

    def add(self):
        self.close()
        self.add_book = Add_Menu()
        self.add_book.show()

    def search(self):
        self.close()
        self.search_book = Search_Menu()
        self.search_book.show()

    def borrow(self):
        self.card_id = Card_ID()
        self.card_id.show()
        self.close()

    def reader(self):
        self.close()
        self.add_reader = Add_Reader()
        self.add_reader.show()

    def beifeng(self):
        flag = db.backups()
        if flag == True:
            button = QMessageBox.about(self, "成功", "")
        else:
            button = QMessageBox.warning(self, "失败", "")

    def huifu(self):
        flag = db.recover()
        if flag == True:
            button = QMessageBox.about(self, "成功", "")
        else:
            button = QMessageBox.warning(self, "失败", "")


class Add_Menu(QWidget, Ui_Dialog3):
    def __init__(self, parent=None):
        super(Add_Menu, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)

    def add(self):
        book_name = self.lineEdit_6.text()
        author = self.lineEdit_7.text()
        book_id = self.lineEdit_8.text()
        version = self.lineEdit_10.text()
        amount = self.lineEdit_5.text()
        book_maker = self.lineEdit_9.text()
        book_id = book_id + '-' + version
        t = db.get_type(book_id[0])
        print([book_id, t, book_name, author,
               book_maker, int(amount), int(amount)])
        if t is not None:
            flag = db.add_book(
                [book_id, t, book_name, author, book_maker, int(amount), int(amount)])
            if flag == True:
                button = QMessageBox.information(self, "成功", "是否重新添加",
                                                 QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
                if button == QMessageBox.Ok:
                    self.close()

                    self.add_menu = Add_Menu()
                    self.add_menu.show()
                else:
                    self.close()
                    self.manager_menu = Manager_Menu()
                    self.manager_menu.show()
            else:
                button = QMessageBox.about(self, "失败", "重新添加")
        else:
            button = QMessageBox.warning(self, "类别不存在", "错误")

    def back(self):
        self.close()
        self.manager_menu = Manager_Menu()
        self.manager_menu.show()


class Add_Reader(QWidget, Ui_Dialog8):
    def __init__(self, parent=None):
        super(Add_Reader, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)

    def add(self):
        stu_no = self.lineEdit_6.text()
        stu_name = self.lineEdit_7.text()
        phone = self.lineEdit_8.text()
        lib_id = self.lineEdit_9.text()

        flag = db.add_reader([stu_no, stu_name, phone, lib_id])
        if flag == True:
            button = QMessageBox.information(self, "成功", "是否重新添加",
                                             QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            if button == QMessageBox.Ok:
                self.close()
                self.add_menu = Add_Reader()
                self.add_menu.show()
            else:
                self.close()
                self.manager_menu = Manager_Menu()
                self.manager_menu.show()
        else:
            button = QMessageBox.about(self, "失败", "重新添加")

    def back(self):
        self.close()
        self.manager_menu = Manager_Menu()
        self.manager_menu.show()


class Search_Menu(QWidget, Ui_Dialog4):
    def __init__(self, parent=None):
        super(Search_Menu, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.search)

    def getbutton(self, id):
        self.QPushButton = QtWidgets.QPushButton("借阅")
        self.QPushButton.setStyleSheet(''' text-align : center;
        background-color : NavajoWhite;
        height : 30px; 
        border-style: outset;
        font : 13px  ''')
        self.QPushButton.clicked.connect(lambda: self.borrow(id))
        return self.QPushButton

    def search(self):
        content = self.lineEdit.text()
        print("sss")
        print(content)
        print(self.comboBox.currentIndex())
        # "数据库搜索"
        # 这是字段，从数据库查询的数据,这里应该返回的是列表，即多个查询结果,要返回str类型
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            ["书名", "作者", "索书号", "出版社", "可借", "馆藏", "事件"])
        self.info = db.book_info(content, int(self.comboBox.currentIndex()))
        if self.info is not None:
            l = len(self.info)
            for i in range(l):
                a = QtWidgets.QTableWidgetItem(self.info[i][0])
                b = QtWidgets.QTableWidgetItem(self.info[i][1])
                c = QtWidgets.QTableWidgetItem(self.info[i][2])
                d = QtWidgets.QTableWidgetItem(self.info[i][3])
                e = QtWidgets.QTableWidgetItem(str(self.info[i][4]))
                f = QtWidgets.QTableWidgetItem(str(self.info[i][5]))
                # g = QtWidgets.QTableWidgetItem(self.pushButton_3)
                self.tableWidget.setItem(i, 0, a)
                self.tableWidget.setItem(i, 1, b)
                self.tableWidget.setItem(i, 2, c)
                self.tableWidget.setItem(i, 3, d)
                self.tableWidget.setItem(i, 4, e)
                self.tableWidget.setItem(i, 5, f)

    def borrow(self, id):
        flag = db.borrow_book(self.info[id][2])
        if flag == True:
            res = self.info[id][4]-1
            self.tableWidget.setItem(
                id, 4, QtWidgets.QTableWidgetItem(str(res)))
        else:
            button = QMessageBox.about(self, "失败", "重新操作")

    def back(self,):
        self.close()
        self.manager_menu = Manager_Menu()
        self.manager_menu.show()


class Search2_Menu(Search_Menu):
    def getbutton(self, id):
        self.QPushButton = QtWidgets.QPushButton("借阅")
        self.QPushButton.setStyleSheet(''' text-align : center;
        background-color : NavajoWhite;
        height : 30px; 
        border-style: outset;
        font : 13px  ''')
        self.QPushButton.clicked.connect(lambda: self.borrow(id))
        return self.QPushButton

    def search(self):
        content = self.lineEdit.text()
        # "数据库搜索"
        # 这是字段，从数据库查询的数据,这里应该返回的是列表，即多个查询结果,要返回str类型
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            ["书名", "作者", "索书号", "出版社", "可借", "馆藏", "事件"])
        self.info = db.book_info(content, int(self.comboBox.currentIndex()))
        if self.info is not None:
            l = len(self.info)
            for i in range(l):
                a = QtWidgets.QTableWidgetItem(self.info[i][0])
                b = QtWidgets.QTableWidgetItem(self.info[i][1])
                c = QtWidgets.QTableWidgetItem(self.info[i][2])
                d = QtWidgets.QTableWidgetItem(self.info[i][3])
                e = QtWidgets.QTableWidgetItem(str(self.info[i][4]))
                f = QtWidgets.QTableWidgetItem(str(self.info[i][5]))
                # g = QtWidgets.QTableWidgetItem(self.pushButton_3)
                self.tableWidget.setItem(i, 0, a)
                self.tableWidget.setItem(i, 1, b)
                self.tableWidget.setItem(i, 2, c)
                self.tableWidget.setItem(i, 3, d)
                self.tableWidget.setItem(i, 4, e)
                self.tableWidget.setItem(i, 5, f)
                self.tableWidget.setCellWidget(i, 6, self.getbutton(i))

    def back(self):
        self.close()
        self.stu_menu = Stu_Menu()
        self.stu_menu.show()


class Card_ID(QWidget, Ui_Dialog5):
    def __init__(self, parent=None):
        super(Card_ID, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.borrow_info)

    def borrow_info(self):
        lib_id = self.lineEdit.text()
        data = db.borrow_info(lib_id)
        if len(data) == 0:
            button = QMessageBox.information(self, "失败", "是否重新输入",
                                             QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            if button == QMessageBox.Ok:
                self.close()
                self.card_id = Card_ID()
                self.card_id.show()
            else:
                self.close()
                self.manager_menu = Manager_Menu()
                self.manager_menu.show()
        else:
            self.close()
            self.info = Borrow_Info()
            self.info.show_info(data)
            self.info.show()


class Borrow_Info(QWidget, Ui_Dialog6):
    def __init__(self, parent=None):
        super(Borrow_Info, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back)

    def show_info(self, info):
        if info is not None:
            l = len(info)
            for i in range(l):
                a = QtWidgets.QTableWidgetItem(info[i][0])
                b = QtWidgets.QTableWidgetItem(info[i][1])
                c = QtWidgets.QTableWidgetItem(info[i][2])
                d = QtWidgets.QTableWidgetItem(format(info[i][3], "%Y-%m-%d"))
                e = QtWidgets.QTableWidgetItem(format(info[i][4], "%Y-%m-%d"))
                # g = QtWidgets.QTableWidgetItem(self.pushButton_3)
                self.tableWidget.setItem(i, 0, a)
                self.tableWidget.setItem(i, 1, b)
                self.tableWidget.setItem(i, 2, c)
                self.tableWidget.setItem(i, 3, d)
                self.tableWidget.setItem(i, 4, e)

    def back(self):
        self.close()
        self.manager_menu = Manager_Menu()
        self.manager_menu.show()


class Borrow2_Info(Borrow_Info):
    def getbutton(self, id):
        self.QPushButton = QtWidgets.QPushButton("续借")
        self.QPushButton.setStyleSheet(''' text-align : center;
        background-color : NavajoWhite;
        height : 30px; 
        border-style: outset;
        font : 13px  ''')
        self.QPushButton.clicked.connect(lambda: self.add_borrow(id))
        self.QPushButton_2 = QtWidgets.QPushButton("归还")
        self.QPushButton_2.setStyleSheet(''' text-align : center;
        background-color : DarkSeaGreen;
        height : 30px; 
        border-style: outset;
        font : 13px  ''')
        self.QPushButton_2.clicked.connect(lambda: self.back_borrow(id))
        widget = QWidget()
        hbox = QHBoxLayout()
        hbox.addWidget(self.QPushButton)
        hbox.addWidget(self.QPushButton_2)
        widget.setLayout(hbox)
        return widget

    def show_info(self, info):
        if info is not None:
            l = len(info)
            self.info = info
            for i in range(l):
                a = QtWidgets.QTableWidgetItem(self.info[i][0])
                b = QtWidgets.QTableWidgetItem(self.info[i][1])
                c = QtWidgets.QTableWidgetItem(self.info[i][2])
                d = QtWidgets.QTableWidgetItem(
                    format(self.info[i][3], "%Y-%m-%d"))
                e = QtWidgets.QTableWidgetItem(
                    format(self.info[i][4], "%Y-%m-%d"))
                # g = QtWidgets.QTableWidgetItem(self.pushButton_3)
                self.tableWidget.setItem(i, 0, a)
                self.tableWidget.setItem(i, 1, b)
                self.tableWidget.setItem(i, 2, c)
                self.tableWidget.setItem(i, 3, d)
                self.tableWidget.setItem(i, 4, e)
                self.tableWidget.setCellWidget(i, 5, self.getbutton(i))

    def add_borrow(self, id):
        time = format(self.info[id][4])
        data = db.add_time(self.info[id][0])
        button = QMessageBox.about(self, "成功", "继续")
        self.close()
        self.borrow_info = Borrow2_Info()
        self.borrow_info.show_info(db.borrow_info(db.lib_id))
        self.borrow_info.show()

    def back_borrow(self, id):
        print("book_id:"+self.info[id][0])
        flag = db.back_book(self.info[id][0])
        if flag == True:
            button = QMessageBox.about(self, "成功", "继续")
            self.close()
            self.borrow_info = Borrow2_Info()
            self.borrow_info.show_info(db.borrow_info(db.lib_id))
            self.borrow_info.show()
        else:
            button = QMessageBox.about(self, "失败", "请稍后重试")

    def back(self):
        self.close()
        self.stu_menu = Stu_Menu()
        self.stu_menu.show()


class Stu_Menu(QWidget, Ui_Dialog2):
    def __init__(self, parent=None):
        super(Stu_Menu, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.borrow)
        self.pushButton_3.clicked.connect(self.info)
        self.pushButton_4.clicked.connect(self.borrow_his)

    def search(self):
        self.close()
        self.search_book = Search2_Menu()
        self.search_book.show()

    def borrow(self):
        self.close()
        self.borrow_info = Borrow2_Info()
        self.borrow_info.show_info(db.borrow_info(db.lib_id))
        self.borrow_info.show()

    def info(self):
        if db.lib_id == "":
            button = QMessageBox.about(self, "错误", "还未注册借阅证")
        else:
            self.close()
            self.stu_info = Info()
            self.stu_info.show()

    def borrow_his(self):
        if db.lib_id == "":
            button = QMessageBox.about(self, "错误", "还未注册借阅证")
        else:
            self.close()
            self.borrow_rec = Borrow_His()
            self.borrow_rec.show()


class Info(QWidget, Ui_Dialog7):
    def __init__(self, parent=None):
        super(Info, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back)
        self.get_info(0)
        self.comboBox.currentTextChanged.connect(
            lambda: self.get_info(self.comboBox.currentIndex()))
        self.pushButton_2.clicked.connect(self.add_money)

    def get_info(self, id):
        self.lineEdit.clear()
        if id == 0:
            info = db.reader_info()
            self.lineEdit.setPlainText(
                "学号："+info[0]+"\n"+"姓名："+info[1]+"\n"+"电话："+info[2]+"\n"+"卡号："+str(info[3])+"\n")
        else:
            info = db.lib_id_info()
            self.lineEdit.setPlainText(
                "卡号："+str(info[0])+"\n"+"余额："+str(info[1]))

    def back(self):
        self.close()
        self.stu_menu = Stu_Menu()
        self.stu_menu.show()

    def add_money(self):
        flag = db.add_money(int(self.lineEdit_2.text()))
        if flag == True:
            button = QMessageBox.about(self, "成功", "充值")
        else:
            button = QMessageBox.warning(self, "失败", "充值")


class Borrow_His(QWidget, Ui_Dialog9):
    def __init__(self, parent=None):
        super(Borrow_His, self).__init__(parent)
        self.setupUi(self)
        self.show_info()
        self.comboBox.currentIndexChanged.connect(
            lambda: self.visual_info(self.comboBox.currentIndex()))
        self.pushButton.clicked.connect(self.back)

    def show_info(self):
        info = db.borrow_record()
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            ["索书号", "书名", "作者", "借阅日期", "归还日期"])
        if info is not None:
            l = len(info)
            for i in range(l):
                a = QtWidgets.QTableWidgetItem(info[i][0])
                b = QtWidgets.QTableWidgetItem(info[i][1])
                c = QtWidgets.QTableWidgetItem(info[i][2])
                d = QtWidgets.QTableWidgetItem(format(info[i][3], "%Y-%m-%d"))
                e = QtWidgets.QTableWidgetItem(format(info[i][4], "%Y-%m-%d"))
                # g = QtWidgets.QTableWidgetItem(self.pushButton_3)
                self.tableWidget.setItem(i, 0, a)
                self.tableWidget.setItem(i, 1, b)
                self.tableWidget.setItem(i, 2, c)
                self.tableWidget.setItem(i, 3, d)
                self.tableWidget.setItem(i, 4, e)
        data = []
        for i in range(l):
            data.append(info[i][0])
        Bin = BingTu()
        Bin.bin(data).render("./pie.html")

    def visual_info(self, id):
        if id == 0:
            self.frame.setVisible(False)
            self.tableWidget.setVisible(True)
        else:
            self.tableWidget.setVisible(False)
            self.hboxLayout.removeWidget(self.myHtml)
            self.myHtml.load(QUrl("file:///D:/编程文件/数据库课设/pie.html"))
            self.hboxLayout.addWidget(self.myHtml)
            self.frame.setVisible(True)

    def back(self):
        self.close()
        self.stu_menu = Stu_Menu()
        self.stu_menu.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mystart = MyStart()
    mystart.show()
    sys.exit(app.exec())
