kelime="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
harflistesi=list()
for i in kelime:
    harflistesi.append(i)
harflistesi.sort()
print(harflistesi)
sozluk=dict()
for i in harflistesi:
    if i in sozluk:
        sozluk[i] +=1
    else:
        sozluk[i]=1
for i,j in sozluk.items():
    print("{} harfi {} defa geçmektedir.".format(i,j))
