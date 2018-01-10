import sqlite3, logging

class Database:

    def __init__(self,db_name):
        self.conn=sqlite3.connect(db_name)
        self.cur=self.conn.cursor()
        logging.basicConfig(filename='mrk_cap_logfile.log', level=logging.DEBUG,
                            format='%s(asctime)s:%(levelname)s:%(message)s')

    def create_table(self,tablename):
        try:
            self.cur.execute("CREATE TABLE IF NOT EXISTS "+tablename+" (name TEXT,change REAL, mktCap REAL, stockprice REAL)")
            self.conn.commit()
            logging.debug("Create Table Successfull:"+tablename)
        except:
            logging.debug("Issue Create Table :" + tablename)

    def insert_data(self,tablename,name, change,mktCap,stockprice):
        try:
            self.cur.execute("INSERT INTO "+tablename+" VALUES (?,?,?,?)",(name,change,mktCap,stockprice))
            self.conn.commit()
            logging.debug("Insert Table Successfull:"+tablename)
        except:
            logging.debug("Issue Insert Table :" + tablename)

    def view_data(self,tablename):
        try:
            self.cur.execute("SELECT * FROM "+tablename)
            rows=self.cur.fetchall()
            logging.debug("View Table Data Successfull:"+tablename)
            return rows
        except:
            logging.debug("Issue In View Table Data :" + tablename)


    def update_data(self,tablename,name,stockprice):
        try:
            self.cur.execute("UPDATE "+tablename+" SET stockprice=? WHERE name=?",(stockprice,name))
            self.conn.commit()
            logging.debug("Update Table Data Successfull:" + tablename)
        except:
            logging.debug("Issue In Update Table Data :" + tablename)


    def search_data(self,tablename,change):
        try:
            self.cur.execute("SELECT * FROM "+tablename+" WHERE change="+change)
            rows = self.cur.fetchall()
            logging.debug("Search Table Data Successfull:" + tablename)
            return rows

        except:
            logging.debug("Issue In Search Table Data :" + tablename)

    def delete_data(self,tablename,name,stockprice):
        try:
            self.cur.execute("DELETE FROM "+tablename+" WHERE name="+name)
            self.conn.commit()
            logging.debug("Update Table Data Successfull:" + tablename)
        except:
            logging.debug("Issue In Update Table Data :" + tablename)


    def delete_all_data(self,tablename):
        try:
            self.cur.execute("DELETE FROM " + tablename)
            self.conn.commit()
            logging.debug("Update Table Data Successfull:" + tablename)
        except:
            logging.debug("Issue In Update Table Data :" + tablename)

    def __del__(self):
        self.conn.close()


