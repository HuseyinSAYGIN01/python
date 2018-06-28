import sqlite3
import datetime
import time
import random
con=sqlite3.connect("veritabani.db")
cursor=con.cursor()
def tolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS degerler(zaman REAL,tarih TEXT,anahtar TEXT,deger REAL)")
def degerekle():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime("%Y-%m-%d %H-%M-%S"))
    anahtar="Python SQLite3"
    deger = random.randrange(0, 10)
    cursor.execute("INSERT INTO degerler(zaman,tarih,anahtar,deger) VALUES (?,?,?,?)",(zaman,tarih,anahtar,deger))
    con.commit()
def degeralyazdir():
    cursor.execute("SELECT * FROM degerler WHERE deger<=5.0")
    data=cursor.fetchall()
    s=1
    for i in data:
        print(s,". satır:",i)
        s +=1
tolustur()
i=0
while (i<10):
    degerekle()
    i +=1
    time.sleep(1)
degeralyazdir()
con.close()
