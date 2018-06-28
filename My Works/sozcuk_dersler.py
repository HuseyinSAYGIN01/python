dersler={"Ahmet":["Programlama Dilleri","Veri Tabanları","Web Tasarım"],"Mehmet":["Grafik Tasarım","Script Dilleri"],"Hakan":["Visual Programlama","Katı Modelleme"]}
isim=input("İsim giriniz: ")
print("{} \'in aldığı dersler:" .format(isim))
for i in (dersler[isim]):
    print(i)