class Dosya():

    def __init__(self,dosya_ismi):

        with open(dosya_ismi,"r",encoding = "utf-8") as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()
            print(kelimeler)

    def dosya_listesi(self,liste_dosyası):
        with open(liste_dosyası,"r",encoding = "utf-8") as file:
            self.dosya_ismi = file.read()


