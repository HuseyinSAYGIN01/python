import requests
birinci=input("Birinci döviz cinsini giriniz.")
ikinci=input("İkinci döviz cinsini giriniz.")
miktar=float(input("Döviz miktarını giriniz."))
link="https://api.fixer.io/latest?base="
response=requests.get(link+birinci)
print(response.content)
veri=response.json()
print(veri["rates"][ikinci]*miktar)



