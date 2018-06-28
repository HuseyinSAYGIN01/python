def faktoriyel(fak):
    if (fak==0):
        return 1
    else:
        for i in range(1,fak):
            fak *=i
        return fak
s=0
while True:
    a=int(input("Faktoriyel değeri giriniz: "))
    b=faktoriyel(a)
    print(b)
    s +=1
    if s==3:
        break
