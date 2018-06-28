import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar=self.menuBar()
        dosya=menubar.addMenu("Dosya")
        duzenle=menubar.addMenu("Düzenle")

        dosya_ac=QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya.addAction(dosya_ac)

        dosya_kaydet=QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        dosya.addAction(dosya_kaydet)

        cikis=QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")
        dosya.addAction(cikis)

        ara_degistir=duzenle.addMenu("Ara ve Değiştir")

        ara=QAction("Ara",self)
        ara_degistir.addAction(ara)

        degistir=QAction("Değiştir",self)
        ara_degistir.addAction(degistir)

        temizle=QAction("Temizle",self)
        duzenle.addAction(temizle)

        cikis.triggered.connect(self.cikis_yap)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("Menüler")
        self.show()

    def cikis_yap(self):
        qApp.quit()
    def response(self,action):
        if action.text()=="Dosya Aç":
            print("Dosya Aç'a basıldı.")
        elif action.text()=="Dosya Kaydet":
            print("Dosya Kaydet'e basıldı.")
        elif action.text()=="Çıkış":
            print("Çıkış'a basıldı.")



app=QApplication(sys.argv)
menu=Menu()
sys.exit(app.exec())