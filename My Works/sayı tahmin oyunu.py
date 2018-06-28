"""
***********************************
Sayı Tahmin Oyunu

1 ile 40 arasında bir sayı giriniz.
***********************************
"""
import random
import time
rasgele_sayi=random.randint(1,40)
tahmin_hakkı=7
while True:
    sayi=int(input("Bir sayı tahmin ediniz"))
    if sayi<rasgele_sayi:
        print("Daha büyük bir sayı giriniz")
        tahmin_hakkı -=1
    elif sayi>rasgele_sayi:
        print("Daha küçük bir sayı giriniz")
        tahmin_hakkı -= 1
    else:
        print("Tebrikler. Tahmin edilen sayı:",rasgele_sayi)
        break
    if tahmin_hakkı==0:
        print("Tahmin hakkınız kalmadı. Tutulan sayı:",rasgele_sayi)
        break

