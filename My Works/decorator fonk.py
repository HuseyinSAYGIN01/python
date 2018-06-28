import time
def zaman_hesapla(fonk):
    def wrapper(sayılar):
        baslangıc=time.time()
        sonuc=fonk(sayılar)
        bitis=time.time()
        print(fonk.__name__+" "+str(bitis-baslangıc)+" "+"saniye sürdü")
        return sonuc
    return wrapper
@zaman_hesapla
def kareleri(sayılar):
    sonuc=list()
    for i in sayılar:
        sonuc.append(i**2)
    return sonuc
@zaman_hesapla
def küpleri(sayılar):
    sonuc=list()
    for i in sayılar:
        sonuc.append(i**3)
    return sonuc
kareleri=kareleri(range(100000))
küpleri=küpleri(range(100000))
for i in kareleri:
    print(i)
for i in range(1000):
    print("******************************************************")
for i in küpleri:
    print(i)