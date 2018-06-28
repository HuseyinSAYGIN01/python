try:
    sayi1=5
    sayi2=1
    print(int(sayi1)/int(sayi2))
except (ValueError,IOError,ZeroDivisionError):
    print("Hata")