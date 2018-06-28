class Ogrenci():
    def derscalis(self):
        print("Öğrenci şu anda ders çalışıyor")
class Calisan():
    def calisan(self):
        print("Personel şu anda çalışıyor")
class Yazilimci(Ogrenci,Calisan):
    pass
yazilimci=Yazilimci()
yazilimci.calisan()
yazilimci.derscalis()
