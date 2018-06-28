liste=[]
s=int(input("Kaç tane eleman girmek istiyorsunuz: "))
sayac=0
while sayac<s:
    liste.append(int(input("Bir sayı giriniz: ")))
    sayac +=1
print(liste)
liste.sort(reverse=True)
print(liste[0])