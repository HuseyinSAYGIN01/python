import requests
from bs4 import BeautifulSoup
def sembolleritemizle(kelimelistesi):
    sembolsuzkelimeler=[]
    semboller="!@'^+%&/()=?_\"<>#${[]}ṡ̇ṡs,.;-"+chr(775)
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
for kelime in kelimelistesi:
    print(kelime)