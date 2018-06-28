print("""********************************
Döngüyle yapsaydık...
liste=[[1,2,3],[4,5,6,7,],[8,9]]
yeni_liste=list()
for i in liste:
    for x in i:
        yeni_liste.append(x)
print(yeni_liste)
List Comprehension ile yapınca
********************************
""")
liste=[[1,2,3],[4,5,6,7,],[8,9]]
yeni_liste=list()
yeni_liste=[x for i in liste for x in i]
print(yeni_liste)
