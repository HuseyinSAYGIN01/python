sayi=int(input("Sayı:"))
liste=list()
toplam=0
"""
for i in str(sayi):
    liste.append(int(i))
for i in liste:
    toplam +=(i**len(liste))
print(toplam)
"""
for i in str(sayi):liste.append(int(i))
for i in liste: toplam +=(i**len(liste))
if toplam==sayi:print(sayi," sayısı armstrong bir sayıdır.")

