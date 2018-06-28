import requests
from bs4 import BeautifulSoup
imdblink="http://www.imdb.com/chart/top"
r=requests.get(imdblink)
soup=BeautifulSoup(r.content,"html.parser")
gelentable=soup.find_all("table",{"class":"chart full-width"})
gelentbody=(gelentable[0].contents)[len(gelentable[0].contents)-2]
gelentr=gelentbody.find_all("tr")
with open("imdb250.txt","a") as dosya:
    for tr in gelentr:
        td=tr.find_all("td",{"class","titleColumn"})
        print((td[0].text).replace("\n",""))
        dosya.write(td[0].text.replace("\n","")+"\n")
