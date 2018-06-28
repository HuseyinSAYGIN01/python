import sqlite3
import time
class Sarkı():
    def __init__(self,adi,sanatci,album,produksiyon,sure):
        self.adi=adi
        self.sanatci=sanatci
        self.album=album
        self.produksiyon=produksiyon
        self.sure=sure
    def __str__(self):
        return "Şarkı ismi: {} \n Sanatçı: {} \n Albüm: {} \n Prodüksiyon= {} \n Süre= {} \n".format(self.adi,self.sanatci,self.album,self.produksiyon,self.sure)
class Metod():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("sarki.db")
        self.cursor=self.baglanti.cursor()
        sorgu="Create Table If not exists sarkilar (adi TEXT,sanatci TEXT,album TEXT,produksiyon TEXT,sure INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def sarkilari_goster(self):
        sorgu="Select * From sarkilar"
        self.cursor.execute(sorgu)
        liste=self.cursor.fetchall()
        if len(liste)==0:
            print("Aradığınız şarkı bulunamadı.")
        else:
            for i in liste:
                sarki=Sarkı(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def sarki_ara(self,isim):
        sorgu="Select * From sarkilar WHERE adi=?"
        self.cursor.execute(sorgu,(isim,))
        liste=self.cursor.fetchall()
        if len(liste) == 0:
            print("Aradığnız şarkı listede yok.")
        else:
            for i in liste:
                sarki=Sarkı(i[0],i[1],i[2],i[3],i[4])
                print(sarki)
    def sarki_ekle(self):
        sorgu="Insert into sakilar VALUES (?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarkı.adi,sarkı.sanatci,sarkı.album,sarkı.produksiyon,sarkı.sure))
        self.baglanti.commit()
    def sarki_sil(self,isim):
        sorgu="Delete from sarkilar WHERE=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()
    def toplam_sure(self,deger1,deger2):
        sozluk={"1":"adi","2":"sanatci","3":"album","4":"produksiyon"}
        sutun=sozluk[deger1]
        deger="Müslüm"
        sorgu = "Select sure From sarkilar WHERE ?=? "
        self.cursor.execute(sorgu,(sutun,deger,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            print("Aradığınız şarkı bulunamadı.")
        else:
            sure=0
            for i in liste:
                sure +=(i[0])
            print(sure)
print("""***********************************
    Şarkı programına hoşgeldiniz.
    İşlemler;
    1-Şarkıları Göster
    2-Şarkı Sorgulama
    3-Şarkı Ekle
    4-Şarkı Sil
    5-Toplam Şarkı Süresi

    Çıkmak için 'q'ya basın..

    **************************************""")
metod=Metod()
while True:
    islem=input("Bir işlem seçiniz: ")
    if (islem=="q"):
        print("Uygulama sonlandırılıyor... \nLütfen bekleyiniz.")
        break
    elif (islem=="1"):
        metod.sarkilari_goster()
    elif (islem=="2"):
        ad=input("Aramak istediğiniz şarkıyı giriniz.")
        metod.sarki_ara(ad)
    elif (islem=="3"):
        print("Eklemek istediğiniz şarkı bilgilerini giriniz.")
        adi=input("Adı: ")
        sanatci=input("Sanatçı: ")
        album=input("Albüm: ")
        produksiyon=input("Prodüksiyon: ")
        sure=input("Süre: ")
        sarkı=Sarkı(adi,sanatci,album,produksiyon,sure)
        metod.sarki_ekle(sarkı)
    elif (islem=="4"):
        isim=input("Silmek istediğiniz şarkı ismini giriniz.")
        metod.sarki_sil(isim)
    elif (islem=="5"):
        while True:
            print("""***********************************
            Şarkıların toplam süresini hesaplamak için bir değer giriniz. Tümü için \'*\' giriniz.
            Arama alanları;
            1-Şarkı adı
            2-Sanatçı adı
            3-Albüm adı
            4-Prodüksiyon
            
            Çıkmak için 'q'ya basın..

            **************************************""")
            try:
                deger1 = input("Hanegi değerde arama yapmak istiyorsunuz?: ")
                deger2 = input("Aranacak kelimeyi giriniz?: ")
                if (deger1 == "*" and deger2 == "*"):
                    metod.toplam_sure(deger1, deger2)
                elif ((deger1 == "*") and (deger2 != "*")) and (int(0) < int(deger2) < int(5)):
                    metod.toplam_sure(deger1, deger2)
                elif ((deger2 == "*") and (deger1 != "*")) and (int(0) < int(deger1) < int(5)):
                    metod.toplam_sure(deger1, deger2)
                elif ((int(0) < int(deger1) < int(5)) and (int(0) < int(deger2) < int(5))):
                    metod.toplam_sure(deger1, deger2)
                elif (deger1 == "Q" or deger1 == "q") or (deger2 == "Q" or deger2 == "q"):
                    break
                else:
                    print("Yanlış değer girdiniz.")
                    islem = input("Yeni bir sorgu yapmak ister misiniz? E/H ?")
                    if (islem == "H" or islem == "h"):
                        break
                    else:
                        break

            except ValueError:
                print("İstenlen bir değer girmediniz.")
                break

    else:
        print("Geçersiz işlem. tekrar deneyiniz.")
