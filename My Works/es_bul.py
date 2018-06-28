class insan():
    def __init__(self,cinsiyet="Null",uyruk="Türkiye",ana_dil="Türkçe",medeni_durum="Bekar",dogum="Null",boy="Null",kilo="Null",ten="Null",goz="Null",sac="Null",egitim="Null",inanc="Null",ydil="Null",meslek="Null",hobi="Null",fobi="Null",saglık="İyi"):
        self.cinsiyet=cinsiyet
        self.uyruk=uyruk
        self.ana_dil=ana_dil
        self.medeni_durum=medeni_durum
        self.dogum=dogum
        self.boy=boy
        self.kilo=kilo
        self.ten=ten
        self.goz=goz
        self.sac=sac
        self.egitim=egitim
        self.inanc=inanc
        self.ydil=ydil
        self.meslek=meslek
        self.hobi=hobi
        self.fobi=fobi
        self.saglık=saglık
    def __str__(self):
        return ("Cinsiyet: {}\nUyruk: {}\nAnadili: {}\nMedeni Durumu: {}\nDoğum Tarihi: {}\nBoyu: {}\nKilosu: {}\nTen Rengi: {}\nGöz Rengi: {}\nSaç Rengi: {}\nEğitimi: {}\nİnancı: {}\nYabancı Dili: {}\nMesleği: {}\nHobileri: {}\nFobileri: {}\nSağlık Durumu".format(self.cinsiyet,self.uyruk,self.ana_dil,self.medeni_durum,self.dogum,self.kilo,self.ten,self.goz,self.sac,self.egitim,self.inanc,self.ydil,self.meslek,self.hobi,self.fobi,self.saglık))
Erkek=insan(cinsiyet="Erkek",medeni_durum="Bekar",boy="175",kilo="95",ten="Esmer",goz="Kahve",sac="Kahve",egitim="Lisans",ydil="İngilizce",meslek="Öğretmnen",hobi=["Kitap","Müzik","Spor"])

Bayan=insan(cinsiyet="Bayan",medeni_durum="Bekar",boy="165",kilo="65",ten="Kumral",goz="Kahve",sac="Kahve",ydil="İngilizce",meslek="Memur",egitim="Lisans",hobi=["Müzik","Kitap","Dans"])



#döngü ile değer alınacak