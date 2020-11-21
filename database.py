import pymysql
class db_t():
    def connectschool(self):
        try:
            cn= pymysql.connect(host="localhost",
                                user="root",
                                password="sepehr1386",
                                db="accounts")
            cr = cn.cursor()
        except:
            print("c")
        finally:
            return cn,cr
            print("cd")
