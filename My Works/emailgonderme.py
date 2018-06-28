import smtplib
content="Merhebe"
server=smtplib.SMTP("smtp.google.com",587) #smtplib kütüphanesinde SMTP fonksiyonunu kullanıyoruz.
server.ehlo()
server.starttls()
server.login("Kullanıcı Adı","Şifre")
server.sendmail("Gönderen","Alıcı",content)
