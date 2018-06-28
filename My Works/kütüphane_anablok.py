from kütüphane import *
print("""***********************************
Kütüphane programına hoşgeldiniz.
İşlemler;
1-Kitapları Göster
2-Kitap Sorgulama
3-Kitap Ekle
4-Kitap Sil
5-Baskı Yükselt

Çıkmak için 'q'ya basın..

********************************************""")
kütüphane=Kütüphane()
while True:
    islem=input("Yapacağınız işlem: ")
    if (islem=="q"):
        print("Program sonlandırılıyor...")
        print("Yine bekleriz.")
        break
    elif (islem=="1"):
        kütüphane.kitaplari_goster()
    elif (islem=="2"):
        isim=input("Soruglamak istediğiniz kitabı girini:")
        kütüphane.kitap_sorgula(isim)
    elif (islem=="3"):
        print("Bilgileri giriniz.")
        isim=input("İsim:")
        yazar=input("Yazar:")
        yayınevi=input("Yayınevi:")
        tür=input("Tür:")
        baskı=int(input("Baskı:"))
        kitap=Kitap(isim,yazar,yayınevi,tür,baskı)
        kütüphane.kitap_ekle(kitap)
    elif (islem=="4"):
        isim=input("İsim:")
        kütüphane.kitap_sil(isim)
    elif (islem=="5"):
        isim=input("Hangi kitabın baskısını yükseltmek istiyorsunuz?\n İsim:")
        kütüphane.baski_yukselt(isim)
    else:
        print("Geçersiz işlem.")