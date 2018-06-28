import sqlite3
import random
import time
import datetime
con=sqlite3.connect("dersler.db")
cursor=con.cursor()
def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (zaman REAL, tarih TEXT, anahtarkelime TEXT, deger REAL)")
def rasgeledegerekle():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime("%Y-%m-%d %H-%M-%S"))
    anahtarkelime="Python Sqlite"
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1(zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()
tabloolustur()
i=0
while (i<10):
    i +=1
    rasgeledegerekle()
    time.sleep(1)
con.close()

