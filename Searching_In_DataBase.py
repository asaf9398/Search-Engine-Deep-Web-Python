import sqlite3 as lt
import sys

print("What do you want to search?")

keyword=raw_input()
con=lt.connect('DataBase.db')
with con:
    cur=con.cursor()
    result=cur.execute("SELECT Websites_Url FROM Websites_To_Search_In WHERE Website_Data LIKE '%"+keyword+"%'")
    con.commit()
    WEBS=(cur.fetchall())
cur.close()
for i in WEBS:
    print (i[0])



