import requests
from bs4 import BeautifulSoup
link="https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w?_ref=infinite"
r=requests.get(link)
soup=BeautifulSoup(r.content,"html.parser")
kelimelistesi=[]
for petiketi in soup.find_all("p"):
    picerik=petiketi.text
    pkelimegruplari=picerik.lower().split()
    for kelime in pkelimegruplari:
        kelimelistesi.append(kelime)
        print(kelime)
with open("kelimelistesi.txt","a") as dosya:
    for i in kelimelistesi:
        dosya.write(i.replace("̇s","s")+"\n")
