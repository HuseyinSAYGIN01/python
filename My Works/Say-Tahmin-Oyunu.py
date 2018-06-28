import time
import random
print("""****************************

Sayı Tahmin Oyununa Hoşgeldiniz

1 ile 40 arasında(1 ve 40 dahil) rastgele tahmin edin.
****************************""")
tahmin_hakkı = 7
rastgele_sayı = random.randint(1,40)

while True:
    tahmin =  int(input("Tahmininiz:"))

    if (tahmin == rastgele_sayı):
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        print("Tebrikler!")
        print("Sayı",rastgele_sayı)
        break
    elif(tahmin < rastgele_sayı):
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha yüksek bir sayı söyleyin.")
        print("Tahmin Hakkı:",tahmin_hakkı)
    else:
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha düşük bir sayı söyleyin.")
        print("Tahmin Hakkı:",tahmin_hakkı)
    if (tahmin_hakkı == 0 ):
        print("Tahmin Hakkınız Bitti. Üzgünüz")
        print("Sayımız:",rastgele_sayı)
        break




