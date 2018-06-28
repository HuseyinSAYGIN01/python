class siir:
    def __init__(self,dosya):
        with open(dosya,"r",encoding="utf-8") as file:
            icerik=file.readlines()
            basharfler=""
            self.satırlar=list()
            for i in icerik:
                i=i.strip()
                i=i.strip("\n")
                basharfler +=i[0]
                self.satırlar.append(i)
            print(basharfler)


dosya=siir("şiir.txt")
