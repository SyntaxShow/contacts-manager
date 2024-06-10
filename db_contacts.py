import sqlite3
class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE if not exists contacts
                         (id integer primary key, fname text, lname text, city text, phone text)
                         """)
        self.con.commit()
        
    def insert(self,fname,lname,city,phone):
        self.cur.execute("""INSERT INTO contacts
                         (id,fname,lname,city,phone)
                         VALUES(null,?,?,?,?)""",(fname,lname,city,phone))
        self.con.commit()
        print('insert record')
        
    def select(self):
        self.cur.execute("SELECT * FROM contacts")
        records = self.cur.fetchall()
        return records
    
    def delete(self,id):
        self.cur.execute("DELETE FROM contacts WHERE id = ?",(id,))
        self.con.commit()
    
    def update(self,id,fname,lname,city,phone):
        self.cur.execute("UPDATE contacts SET fname=? , lname=? , city=? , phone=? where id=?",(fname,lname,city,phone,id))
        self.con.commit()
    
    def search(self,input_):
        self.cur.execute("""SELECT * FROM contacts WHERE
                         fname=? or lname=? or city=? or phone=?
                         """,(input_,input_,input_,input_))
        records = self.cur.fetchall()
        return records