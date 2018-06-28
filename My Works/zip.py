liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
i=0
sonuc=list()
while (i<len(liste1)) and (i<len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i +=1
print(sonuc)

#zip fonksiyonu ile
print("*****zip fonksiyonu ile*****")
print(list(zip(liste1,liste2)))

#farklı bir örnek
print("***farklı bir zip fonksin örneği***")
listem1 = [1,2,3,4]
listem2 = ["Python","Php","Java","Javascript"]

for i,j in zip(listem1,listem2):
    print("i:",i,"j:",j)

# Sözlükleri zipleyelim
print("***farklı bir zip fonksin örneği***")
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}
print(list(zip(sözlük1,sözlük2)))

# Sözlükleri zipleyelim
print("***farklı bir zip fonksin örneği***")
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}
print(list(zip(sözlük1.values(),sözlük2.values())))

