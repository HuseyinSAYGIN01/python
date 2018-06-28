def liste_yazdir(liste):
    sira=1
    for x in liste:
        print(sira,". eleman: ",x,"\n")
        sira +=1
def sozluk_yazdir(sozluk):
    sira=1
    for x,j in sozluk.items():
        print(sira,". eleman: ",x+" ",j,"\n")
        sira +=1

while True:
    secim = int(input("Liste oluşturmak için 1'i, sözlük oluşturmak için 2'yi giriniz."))
    if secim==1:
        listem = []
        while True:
            eleman = input("Bir eleman giriiz: ")
            if (eleman == "bitir"):
                break
            else:
                listem.append(eleman)
        liste_yazdir(listem)
    elif secim==2:
        sozluk = {}
        while True:
            anahtar = input("Anahtar kelimeyi giriniz: ")
            deger = input("Değer giriniz: ")
            if (anahtar == "bitir" or deger == "bitir"):
                break
            else:
                sozluk[anahtar]=deger
        sozluk_yazdir(sozluk)
    else:
        print("Geçerli bir giriş yapmadınız.")
    break





