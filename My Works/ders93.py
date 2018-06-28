class Dosya:
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerigi=file.read()
            kelimeler=dosya_icerigi.split()
            self.sade_kelimeler=list()
            for i in kelimeler:
                i=i.strip("/n")
                i=i.strip(".")
                i=i.strip(",")
                i=i.strip(" ")
                self.sade_kelimeler.append(i)
    def tum_kelimeler(self):
        tum_kelimeler=set()
        for i in self.sade_kelimeler:
            tum_kelimeler.add(i)
        for i in tum_kelimeler:
            print(i)
    def kelime_frekansı(self):
        kelime_sozluk=dict()
        for i in self.sade_kelimeler:
            if i in kelime_sozluk:
                kelime_sozluk[i] +=1
            else:
                kelime_sozluk[i]=1
        print("Kelime frekansı...................")
        for i,j in kelime_sozluk.items():
            print("{} kelimesi {} defa geçmektedir.".format(i,j))
dosya=Dosya()
dosya.kelime_frekansı()