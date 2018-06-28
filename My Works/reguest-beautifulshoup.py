import requests
from bs4 import BeautifulSoup
url="http://sirketarama.com/arama.asp?s=1&ara=lokanta"
response=requests.get(url)
html_içeriği=response.content
soup=BeautifulSoup(html_içeriği,"html.parser")
for i in (soup.find_all("a")):
    link=i.get("href")
    if (link[0:7])=="sirket.":
        print(i.text)