def ozyenileme(listele):
    if len(listele)<3:
        print(listele)
        return 1
    else:
        return listele[2] * (ozyenileme(listele[3:]))
def ekle(f):
    listeyap=[]
    for i in range(0,f+1):
        listeyap=listeyap+[i]
    return listeyap
while True:
    a=ekle(int(input("Faktoriyel giriniz: ")))
    #print(a)
    print(ozyenileme(a))