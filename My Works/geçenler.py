def hesapla(satır):
    satır=satır[:-1]
    liste=satır.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    son_not=not1*(3/10)+not2*(3/10)+not3*(4/10)
    if (son_not>=90):
        harf_notu="AA"
    elif (son_not>=85):
        harf_notu="BA"
    elif (son_not >= 80):
        harf_notu = "BB"
    elif (son_not >= 75):
        harf_notu = "CB"
    elif (son_not >= 70):
        harf_notu = "CC"
    elif (son_not >= 65):
        harf_notu = "DC"
    elif (son_not >= 60):
        harf_notu = "DD"
    elif (son_not >= 55):
        harf_notu = "FD"
    else:
        harf_notu="FF"
    return isim+"--------------->>"+harf_notu+"\n"

with open("dosya.txt","r",encoding="utf-8") as file:
    kalanlar=[]
    gecenler=[]
    for i in file:
        kontrol=hesapla(i)
        if (kontrol[-3]=="F"):
            kalanlar.append(kontrol)
        else:
            gecenler.append(kontrol)
    with open("geçenler.txt","w",encoding="utf-8") as file2:
        for i in gecenler:
            file2.write(i)
    with open("kalanlar.txt","w",encoding="utf-8") as file3:
        s=1
        for i in kalanlar:
            file3.write(i)
