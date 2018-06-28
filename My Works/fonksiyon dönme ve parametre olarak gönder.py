def anafonk(islem_adı):
    def toplama(*args):
        toplam=0
        for i in args:
            toplam +=i
        return toplam
    def carpma(*args):
        carpım=1
        for i in args:
            carpım *=i
        return carpım
    if islem_adı=="toplama":
        return toplama
    else:
        return carpma
islem=input("\'toplama\' ya da \'carpma\' yazarak işlem seçin ")
fonk=anafonk(islem)
print(fonk(1,2,3))

def toplama(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carpma (a,b):
    return a*b
def bolme(a,b):
    return a/b
def anafonk2(fonk1,fonk2,fonk3,fonk4,islem):
    if islem=="toplama":
        print(fonk1(4,5))
    elif islem=="cıkarma":
        print(fonk2(5,4))
    elif islem=="carpma":
        print(fonk3(4,5))
    elif islem=="bolme":
        print(fonk4(10,2))
    else:
        print("Geçersiz işlem")
islemim=input("İşlem gir: ")
anafonk2(toplama,cıkarma,carpma,bolme,islemim)
