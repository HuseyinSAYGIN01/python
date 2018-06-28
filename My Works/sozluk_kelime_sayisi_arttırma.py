kelimeler={}
while True:
    kelime=input("Bir kelime giriniz")
    if kelime=="yazdır":
        print(kelimeler)
        break
    elif kelime in kelimeler:
        kelimeler[kelime] +=1
    else:
        kelimeler[kelime]=1
