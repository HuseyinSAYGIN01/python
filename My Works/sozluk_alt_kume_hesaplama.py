import math
def hesapla(eleman_sayisi,alt_elm_say):
    print("Alt Küme Sayısı: ",(2**eleman_sayisi))
    print("Öz alt küme sayısı",((2**eleman_sayisi-1)))
    print(alt_elm_say,"elemanlı alt küme sayısı: ",((math.factorial(eleman_sayisi))/(((math.factorial(eleman_sayisi-alt_elm_say)))*(math.factorial(alt_elm_say)))))

while True:
    try:
        while True:
            eleman_sayisi=int(input("Kümenin eleman sayısını giriniz:"))
            if (eleman_sayisi<0):
                print("Sıfır ya da daha büyük bir sayı giriniz.")
            else:
                break
        while True:
            alt_elm_say = int(input("Kaç elemanlı alt kümeleri hesaplatmak istediğinizi giriniz."))
            if alt_elm_say < 0:
                print("Sıfır yada daha büyük bir sayı giriniz.")
            elif alt_elm_say>eleman_sayisi:
                print("Alt kümenin eleman sayısı Öz kümenin eleman sayısından fazla olamaz.")
            else:
                break
        if eleman_sayisi>=0 and alt_elm_say>=0 and alt_elm_say<=eleman_sayisi:
            break

    except:
        print("Girilen değerler sayı olmalı")


if alt_elm_say==0:
    print("0 elemanlı bir kümenin 0 elemanlı alt küme sayısı 0'dır")
else:
    print(hesapla(eleman_sayisi,alt_elm_say))
