import requests
from bs4 import BeautifulSoup
import operator
def sozlukolustur(kelimelistesi):
    kelimesayisi={}
    for kelime in kelimelistesi:
        if kelime in kelimesayisi:
            kelimesayisi[kelime] += 1
        else:
            kelimesayisi[kelime] = 1
    return kelimesayisi

def sembolleritemizle(kelimelistesi):
    sembolsuzkelimeler=[]
    semboller="!@'^+%&/()=?_\"<>#${[]},.;-"+chr(775)
    for kelime in kelimelistesi:
        for sembol in semboller:
            if sembol in kelime:
                kelime=kelime.replace(sembol,"")
        if (len(kelime)>0):
            sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler
link="https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w?_ref=infinite"
r=requests.get(link)
soup=BeautifulSoup(r.content,"html.parser")
kelimelistesi=[]
for petiketi in soup.find_all("p"):
    picerik=petiketi.text
    pkelimegruplari=picerik.lower().split()
    for kelime in pkelimegruplari:
        kelimelistesi.append(kelime)
        #print(kelime)
kelimelistesi=sembolleritemizle(kelimelistesi)
kelimesayisi=sozlukolustur(kelimelistesi)
#for anahtar,deger in kelimesayisi.items():
#    print(str(deger)+" "+str(anahtar))
for anahtar,deger in sorted(kelimesayisi.items(),key=operator.itemgetter(1)):
    print(anahtar,deger)