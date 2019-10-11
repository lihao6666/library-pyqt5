import pymysql
import traceback
import os

class mydb():
    login_id=""
    lib_id=""
    def db_connect(self):
        db = pymysql.connect(host='127.0.0.1',user='lh', password='lh19990507', port=3306,db='library')
        return db
    def login(self,id,passwd,previ):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = "select passwd from users where stu_no=%s and privilege=%s"
            cursor.execute(sql,[id,previ])
            data = cursor.fetchone()
        except :
            db.rollback()
            return False
        else:
            if data is None:
                return False
            elif passwd == data[0]:
                self.login_id = id
                sql = "select lib_id from reader where stu_no=%s"
                cursor.execute(sql,[id])
                data = cursor.fetchone()
                if data is not None:
                    self.lib_id = data[0]
                return True
            else:
                return False
        db.close()
    def register(self,id,passwd,previ):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = 'insert into users values(%s,%s,%s)'
            cursor.execute(sql,[id,passwd,previ])
            db.commit()
        except :
            traceback.print_exc()
            db.rollback()
            return False
        else:
            return True
        db.close()
    def add_reader(self,info):
        print(info)
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = 'insert into lib_card values(%s,15.0)'
            cursor.execute(sql,[info[3]])
            sql = 'insert into reader values(%s,%s,%s,%s)'
            cursor.execute(sql,info)
            db.commit()
        except:
            traceback.print_exc()
            db.rollback()
            return False
        else:
            return True
    def book_info(self,bn,signal):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            if signal == 0:
                print(bn)
                sql = "select book_name,author,book_id,press,amount,total from book where book_name like '%%%%%s%%%%'"
                sql = sql %(bn)
                cursor.execute(sql)
                data = cursor.fetchall()
                print(data)
                print(cursor.rowcount)
            else:
                sql = "select book_name,author,book_id,press,amount,total from book where type=%s"
                cursor.execute(sql,[bn])
                data = cursor.fetchall()
                print(data)
                print(cursor.rowcount)
        except:
            traceback.print_exc()
            db.rollback()
        else:
            return list(data)   
        db.close()
    def borrow_book(self,book_id):
        db = self.db_connect()
        cursor = db.cursor()
        
        
        try:
            sql = 'select curdate()'
            cursor.execute(sql)
            s_time = cursor.fetchone()[0]
            sql = 'select date_add(%s,interval 30 day)'
            cursor.execute(sql,[s_time])
            d_time = cursor.fetchone()[0]
        except:
            traceback.print_exc()
            db.rollback()
            return False
        else:
            try:
                sql = 'insert into borrow values(%s,%s,%s,%s)'
                cursor.execute(sql,[self.lib_id,book_id,s_time,d_time])
                db.commit()
            except:
                traceback.print_exc()
                db.rollback()
                return False
            else:
                return True
            db.close()
    def borrow_info(self,lib_id):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = 'call reader_borrow_info(%s)'
            cursor.execute(sql,[lib_id])
            data = cursor.fetchall()
            print(data)
        except:
            traceback.print_exc()
            db.rollback()
        else:
            return list(data)
        db.close()
    def back_book(self,book_id):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = 'select curdate()'
            cursor.execute(sql)
            time = cursor.fetchone()[0]
            sql = 'select ddl from borrow where book_id=%s and ddl>%s'
            cursor.execute(sql,[book_id,time])
            data = cursor.fetchone()

        except:
            traceback.print_exc()
            db.rollback()
            return False
        else:
            try:
                sql = 'delete from borrow where book_id=%s'
                cursor.execute(sql,[book_id])
                db.commit()
            except:
                traceback.print_exc()
                db.rollback()
                return False
            else:
                if data is None:
                    self.over_time(self.lib_id)
                return True
        db.close()
    def over_time(self,lib_id):
        print("SSS")
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = 'update lib_card set balance=balance-1.0 where lib_id=%s'
            cursor.execute(sql,[lib_id])
            db.commit()
        except:
            traceback.print_exc()
            db.rollback()
        else:
            pass
        db.close()              
    def add_time(self,book_id):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = ''
            cursor.execute(sql,[book_id])
            db.commit()
        except:
            traceback.print_exc()
            db.rollback()
            return False
        else:
            return True

        db.close()
    def add_book(self,info):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = 'insert into book(book_id,type,book_name,author,press,amount,total)values(%s,%s,%s,%s,%s,%s,%s) on duplicate key update total=total+values(total),amount=amount+values(amount)'
            cursor.execute(sql,info)
            db.commit()
        except:
            traceback.print_exc()
            db.rollback()
            return False
        else:
            return True
        db.close()
    def reader_info(self):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = 'select stu_no,stu_name,phone,lib_id from reader where lib_id=%s'
            cursor.execute(sql,[self.lib_id])
            data = cursor.fetchone()
        except:
            traceback.print_exc()
            db.rollback()
        else:
            print(data)
            print(list(data))
            return list(data)
        db.close()
    def lib_id_info(self):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = 'select lib_id,balance from lib_card where lib_id=%s'
            cursor.execute(sql,[self.lib_id])
            data = cursor.fetchone()
            print(data)
        except:
            traceback.print_exc()
            db.rollback()
        else:
            return list(data)
        db.close()
    def backups(self):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            os.system("mysqldump --host 111.230.138.45  -P 3306 -u lh -plh19990507 library > mydb.sql")
        except:
            traceback.print_exc()
            db.rollback()
            return False
        else:
            return True
        db.close()
            

    def recover(self):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            os.system("mysql --host 111.230.138.45  -P 3306 -u lh -plh19990507 library < mydb.sql")
        except:
            traceback.print_exc()
            db.rollback()
            return False
        else:
            return True
        db.close()
    def add_money(self,money):
        db = self.db_connect()
        cursor = db.cursor()
        try:
            sql = "update lib_card set balance=balance+%s where lib_id=%s"
            cursor.execute(sql,[money,self.lib_id])
            db.commit()
        except:
            traceback.print_exc()
            db.rollback()
            return False
        else:
            return True
        db.close()
    def get_type(self,info):
        db = self.db_connect()
        cursor = db.cursor()

        try:
            sql = "select type from category where type_num=%s"
            cursor.execute(sql,[info])
            data = cursor.fetchone()
            print(data)
        except:
            traceback.print_exc()
            db.rollback()
        else:
            return list(data)
        db.close()
    def borrow_record(self):
        db = self.db_connect()
        cursor = db.cursor()

        try:
            sql = "call reader_borrow_his_info(%s)"
            cursor.execute(sql,[self.lib_id])
            data = cursor.fetchall()
            print(data)
        except:
            traceback.print_exc()
            db.rollback()
        else:
            return list(data)


