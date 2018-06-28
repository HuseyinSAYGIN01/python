import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
mesaj=MIMEMultipart()
mesaj["From"]=["huseyinkirik01@gmail.com"]
mesaj["To"]=["huseyinkirik01@gmail.com"]
mesaj["Subject"]=["Smtp mail gönderme"]
yazi="""
Bu mail smtp ile gönderilmiştir.
Hüseyin KIRIK
"""
mesaj_gövdesi=MIMEText(yazi,"plain")
mesaj.attach(mesaj_gövdesi)
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("huseyinkirik01@gmail.com","Kirik.089130630")
mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
print("Mail başarıyla gönderildi.")
