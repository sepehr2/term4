import mysql.connector


class Database:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
            db='schoolManagement',
            user='root',
            password='sepehr1386',
            host='localhost'
            )
            self.cr = self.db.cursor()
        except:
            print('Error in Connection to DB')


class StudentInsert(Database):
    def __init__(self, name, family, birthDate, nationalCode, address):
        Database.__init__(self)
        data = (name, family, birthDate, nationalCode, address)
        query = """INSERT INTO student
        (name, family, birthDate, nationalCode, address)
        VALUES
        (%s,%s,%s,%s,%s)"""

        self.cr.execute(query, data)
        self.db.commit()
        
        self.cr.close()
        self.db.close()


class StudentDelete(Database):
    def __init__(self, id):
        Database.__init__(self)
        data = (id,)
        query = "DELETE FROM student WHERE id=%s"

        self.cr.execute(query, data)
        self.db.commit()

        self.cr.close()
        self.db.close()


class StudentUpdate(Database):
    def __init__(self, name, family, n_id,birth,addr,id):
        Database.__init__(self)
        
        data = (name, family, n_id,birth,addr,id)
        query = """UPDATE student   
        SET name = %s, family = %s,nationalCode = %s, birthDate = %s ,  address = %s
        WHERE id= %s"""
        
        self.cr.execute(query, data)
        self.db.commit()

        self.cr.close()
        self.db.close()


class StudentSelect(Database):
    def __init__(self):
        Database.__init__(self)

        query = "SELECT * FROM student"

        self.cr.execute(query)
        self.result = self.cr.fetchall()

        self.cr.close()
        self.db.close()
    def get(self):
        return self.result

class StudentGet(Database):
    def __init__(self,id):
        Database.__init__(self)

        query = "SELECT * FROM student where id=%s" % id

        self.cr.execute(query)
        self.result = self.cr.fetchall()

        self.cr.close()
        self.db.close()

    def get(self):
        return self.result

class StudentSearch(Database):
    def __init__(self, name, family):
        Database.__init__(self)

        name = '%' + name +'%'
        family = '%' + family +'%'
        data = (name, family)
        query = """SELECT * FROM student
        WHERE name LIKE %s and family LIKE %s"""
        
        self.cr.execute(query, data)
        self.result = self.cr.fetchall()

        self.cr.close()
        self.db.close()

    def get(self):
        return self.result


class GradeInsert(Database):
    def __init__(self, studentId, math, physics,chemistry, history, programming):
        Database.__init__(self)
        data = (studentId, math, physics,chemistry, history, programming)
        query = """INSERT INTO grade
        (studentId, math, physics, chemistry, history, programming)
        VALUES
        (%s,%s,%s,%s,%s,%s)"""
        
        self.cr.execute(query, data)
        self.db.commit()
        
        self.cr.close()
        self.db.close()
        


class GradeSearch(Database):
    def __init__(self, studenId):
        Database.__init__(self)
        data = (studenId,)
        query = "SELECT * FROM grade WHERE studentId=%s"
        
        self.cr.execute(query, data)
        self.result = self.cr.fetchall()

        self.cr.close()
        self.db.close()

    def get(self):
        return self.result