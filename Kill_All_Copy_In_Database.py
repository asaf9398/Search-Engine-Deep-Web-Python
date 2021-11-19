import sqlite3 as lt
import sys
con=lt.connect('DataBase.db')
with con:
    cur=con.cursor()
    cur.execute("SELECT DISTINCT Websites_Url FROM Websites_To_Search_In")
cur.close()
