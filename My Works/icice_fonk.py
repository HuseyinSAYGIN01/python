def fonk(*args):
    def topla(args):
        toplam=0
        for i in args:
            toplam +=i
        return toplam
    print(topla(args))
def selamla(isim):
    def merhaba(ad):
        print("Merhaba",ad)
    merhaba(isim)
selamla("Hüseyin")

fonk(1,2,3,4,5)