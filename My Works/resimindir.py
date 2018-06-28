import urllib.request
url1="https://storage.googleapis.com/gweb-uniblog-publish-prod/static/blog/images/google-200x200.7714256da16f.png"
url2="http://www.prbilisim.com/resimler/diger/271_20161126141242.jpg"
url3="https://www.omrckr.com/solaris/upload/2827888499730.png"
urllistesi=[url1,url2,url3]
s=0
for url in urllistesi:
    s +=1
    urllib.request.urlretrieve(url,"Resim"+str(s)+".jpg")
