import random


class dusman:
    def __init__(self, isim="Düşman", kalan_can=100, saldiri_gucu=50, mermi_sayisi=30):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim, " saldırıyor.")
        harcanan_mermi = random.randrange(0, 10)
        print(harcanan_mermi, " mermi harcandı.")
        self.mermi_sayisi -= harcanan_mermi
        return (harcanan_mermi, self.saldiri_gucu)

    def saldiriyaugra(self, harcanan_mermi, saldiri_gucu):
        print("Vuruldum")
        self.kalan_can -= (harcanan_mermi * saldiri_gucu)

    def mermibittimi(self):
        if (self.mermi_sayisi <= 0):
            print(self.isim + " Konuşuyor:Mermim bitti. Oyundan çıkıyorum.")
            return True
        print(str(self.mermi_sayisi)+" Mermi kaldı.")
        return False

    def hayattami(self):
        if (self.kalan_can <= 0):
            print("Ölüyorummm.")
        else:
            print(str(self.kalan_can)+" can kaldı")

    def yazdir(self):
        print("Bilgilendirme....................")
        print("İsim: ", self.isim, "Kalan Can: ", self.kalan_can, "Saldırı Gücü: ", self.saldiri_gucu, "Mermi Sayısı: ",
              self.mermi_sayisi)


dusmanlar = []
i = 0
while i < 10:
    rasgelecan = random.randrange(100, 200)
    rasgeleguc = random.randrange(10, 20)
    rasgelemermi = random.randrange(20, 30)
    yenidusman = dusman("Dusman" + str(i + 1), rasgelecan, rasgeleguc, rasgelemermi)
    dusmanlar.append(yenidusman)
    i += 1
for dusman in dusmanlar:
    dusman.yazdir()
    dusman.saldir()
    dusman.mermibittimi()
    dusman.hayattami()
