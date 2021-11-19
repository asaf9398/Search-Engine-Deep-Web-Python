import sqlite3 as lt
import sys
con=lt.connect('DataBase.db')
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE Websites_To_Search_In(ID INT,Websites_Url TEXT,Website_Data TEXT)")
cur.close()
