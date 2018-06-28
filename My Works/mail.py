with open("mail.txt","r",encoding="utf-8") as file:
    for satır in file:
        satır = satır[:-1]
        if (satır.endswith(".com") and satır.find("@") != -1):
            print(satır)