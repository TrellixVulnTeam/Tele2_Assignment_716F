import sqlite3

class Database:

    def __init__(self,db_name):
        self.conn=sqlite3.connect(db_name)
        self.cur=self.conn.cursor()

    def create_table(self,tablename):
        self.cur.execute("CREATE TABLE IF NOT EXISTS "+tablename+" (name TEXT,change REAL, mktCap REAL, stockprice REAL)")
        self.conn.commit()

    def insert_data(self,tablename,name, change,mktCap,stockprice):
        self.cur.execute("INSERT INTO "+tablename+" VALUES (?,?,?,?)",(name, change,mktCap,stockprice))
        self.conn.commit()

    def view_data(self,tablename):
        self.cur.execte("SELECT * FROM "+tablename)
        rows=self.cur.fetchall()
        return rows

    def update_data(self,tablename,name,stockprice):
        self.cur.execute("UPDATE "+tablename+" SET stockprice=? WHERE name=?", (name, stockprice))
        self.conn.commit()

    def search_data(self,tablename,change):
        self.cur.execte("SELECT * FROM "+tablename+" WHERE change="+change)
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()