import sqlite3 as lt
import sys
def Insert_Data_To_DataBase(id,url,data):
    con=lt.connect('DataBase.db')
    with con:
        cur=con.cursor()
        cur.execute("INSERT INTO Websites_To_Search_In(ID,Websites_Url,Website_Data) VALUES ('{0}','{1}','{2}')".format(id,url,data))
    cur.close()


Insert_Data_To_DataBase(1,"www.google.com","S")