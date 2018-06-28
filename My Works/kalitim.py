class Calisan():
    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının yapıcı fonksiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgiler(self):
        print("Bilgiler:\n","İsim:",self.isim,"Maaş:",self.maas,"Departman:",self.departman)
    def zam(self,miktar):
        self.maas +=miktar
    def degis(self,yeni):
        self.departman=yeni
class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi):
        print("Yönetici sınıfının yapıcı fonksiyonu")
        super().__init__(isim,maas,departman)
        self.kisi=kisi
    def bilgiler(self):
        print("Yönetici sınıfının bilgileri gösteriliyor")
        print("Bilgiler\n","İsim:",self.isim,"Maaş:",self.maas,"Departman:",self.departman,"Kişi:",self.kisi)
    def kisiarttir(self,artis):
        print("Kişi sayısı arttırılıyor")
        self.kisi +=artis
yonetici=Yonetici("Hüseyin",3000,"Fatih Projesi",200)
yonetici.bilgiler()
yonetici.kisiarttir(10)
yonetici.bilgiler()


