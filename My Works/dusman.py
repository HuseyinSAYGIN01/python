class dusman:
    def __init__(self, isim="Düşman", kalan_can=100, saldiri_gucu=50, mermi_sayisi=30):
        self.isim=isim
        self.kalan_can=kalan_can
        self.saldiri_gucu=saldiri_gucu
        self.mermi_sayisi=mermi_sayisi
    def yazdir(self):
        print("Bilgilendirme....................")
        print("İsim: ",self.isim,"Kalan Can: ", self.kalan_can,"Saldırı Gücü: ",self.saldiri_gucu,"Mermi Sayısı: ",self.mermi_sayisi)
dusman1=dusman((str(input("Düşma1 için isim giriniz: "))),500,100,50)
dusman2=dusman((str(input("Düşman2 için isim giriniz: "))),300,80,40)
dusman3=dusman()
while True:
    a=(int(input("Düşman bilgisi yazdırmak için bir sayı giriniz (1,2,3)")))
    if (a==1):
        dusman1.yazdir()
    elif (a==2):
        dusman2.yazdir()
    elif (a==3):
        dusman3.yazdir()
    else:
        print("İstenilen değerlerden birini giriniz.")
