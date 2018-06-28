import random
import time

class Kumanda():
    def __init__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if (self.tv_durum=="açık"):
            print("Televizon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum="açık"
    def tv_kapat(self):
        if (self.tv_durum=="kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...")
            self.tv_durum="kapalı"
    def ses_ayarları(self):
        while True:
            cevap=input("Sesi azalt:'<'\nSesi arttır:'>'\nÇıkış:çıkış")
            if (cevap=="<"):
                if (self.tv_ses!=0):
                    self.tv_ses -=1
                    print("Ses:",self.tv_ses)
            elif (cevap==">"):
                if (cevap!=100):
                    self.tv_ses +=1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses güncellendi",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi...")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki Kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv Durumu: {}\nTv Sesi: {}\nKanal Lisetesi: {}\nŞu anki kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
kumanda=Kumanda()
print("""
Televizyon Uygulaması

1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rasgele Kanala Geç

7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.

""")

while True:
    işlem=input("Bir işlem seçiniz:")
    if (işlem=="q"):
        print("Kumandadan çıkılıyor...")
        time.sleep(1)
        break
    elif (işlem=="1"):
        kumanda.tv_ac()
    elif (işlem=="2"):
        kumanda.tv_kapat()
    elif (işlem=="3"):
        kumanda.ses_ayarları()
    elif (işlem=="4"):
        kanal_isimleri=input("Eklenecek kanalları ',' ile ayırarak giriniz: ")
        eklenecekler=kanal_isimleri.split(",")
        for ekle in eklenecekler:
            kumanda.kanal_ekle(ekle)
    elif (işlem=="5"):
        print("Kanal sayısı: ",len(kumanda))
    elif (işlem=="6"):
        kumanda.rastgele_kanal()
    elif (işlem=="7"):
        print(kumanda)
    else:
        print("Geçersiz işlem...")







