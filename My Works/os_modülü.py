import os
from datetime import datetime
def liste_yap(yol):
    yollar = list()
    klasörler = list()
    dosyalar = list()
    for i, j, k in os.walk(yol):
        yollar.append(i)
        klasörler.append(j)
        dosyalar.append(k)
    secim=input("Seçiminiz(yollar,klasörler,dosyalar): ")
    if secim=="yollar":
        return yollar
    elif secim=="klasörler":
        return klasörler
    elif secim=="dosyalar":
        return dosyalar
    else:
        return "geçerli bir seçim girmediniz"
while True:
    yol = "c:/Users/HuseyinKIRIK/Desktop"
    fonk = liste_yap(yol)
    if fonk == "geçerli bir seçim girmediniz":
        print("Geçerli bir seçim girmediniz.")
    else:
        for i in fonk:
            print(i)

