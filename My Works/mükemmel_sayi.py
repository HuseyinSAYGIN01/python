
while True:
    sayi = int(input("Bir sayı giriniz: "))
    if  sayi<=1:
        print("Geçerli bir sayı giriniz.")
    else:
        break
liste=list()
for i in range(1,sayi):
    if sayi%i==0 :
        liste.append(i)
toplam=0
for i in liste:
    toplam +=i
if  toplam==sayi:
    print("{} sayısının tam bölenleri {} sayılarıdır. {} sayısı mükemmel bir sayıdır.".format(sayi,liste,sayi))
else:
    print("{} sayısının tam bölenleri {} sayılarıdır. {} sayısı mükemmel bir sayı değildir.".format(sayi, liste, sayi))



