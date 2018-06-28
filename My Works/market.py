import sqlite3
import datetime
import locale
locale.setlocale(locale.LC_ALL,'')
an=datetime.datetime.today()
tarih=datetime.datetime.strftime(an,'%c')
print(tarih)