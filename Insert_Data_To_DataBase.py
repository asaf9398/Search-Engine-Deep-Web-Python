import sqlite3 as lt
import sys
con=lt.connect('DataBase.db')
with con:
    cur=con.cursor()
    cur.execute("INSERT INTO Websites_To_Search_In VALUES(3,'Website3','TEXT3')")
cur.close()
