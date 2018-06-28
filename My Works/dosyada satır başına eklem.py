with open("huseyin.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    kelime=input("Kelime gir: ")+"\n"
    sayac=0
    file.seek(0)
    for satır in liste:
        if ((kelime)==satır):
            sayac +=1
            print(sayac," adet aynı satırdan mevcut.")
    if (sayac==0):
        liste.insert(0,kelime)
    #for i in liste:
        #file.write(i)
    file.writelines(liste)
