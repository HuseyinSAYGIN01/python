def kontrol(sayi):
    if (sayi % 2 != 0):
        raise ValueError
    else:
        return sayi
liste=[2,16,18,3,4,5,6,7,54,45,76,89,24]
yeni_liste=list()
for i in liste:
    try:
        yeni_liste.append(kontrol(i))
    except:
        pass
yeni_liste.sort(reverse=True)
print(yeni_liste)