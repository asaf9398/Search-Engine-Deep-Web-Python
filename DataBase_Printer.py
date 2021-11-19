import sqlite3 as lt
import sys
con=lt.connect('DataBase.db')
with con:
    cur=con.cursor()
    cur.execute("SELECT * FROM Websites_To_Search_In")
    rows=cur.fetchall()
    for x in rows:
        print(x)
cur.close()
