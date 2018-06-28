import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QAction,qApp,QMainWindow
import tkinter
from tkinter import messagebox
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani=QTextEdit()
        self.temizle=QPushButton("Temizle")
        self.ac=QPushButton("Aç")
        self.kaydet=QPushButton("Kaydet")
        h_box=QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)
        v_box=QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("Not Defteri")
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
        self.show()
    def yaziyi_temizle(self):
        self.yazi_alani.clear()
    def dosya_ac(self):
        try:
            dosya_ismi=QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
            with open(dosya_ismi[0],"r") as file:
                self.yazi_alani.setText(file.read())
        except:
            root=tkinter.Tk()
            root.withdraw()
            messagebox.showinfo("Bilgilendirme","İşlem iptal edildi.")
    def dosya_kaydet(self):
        dosya_ismi=QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Pencere()
        self.setCentralWidget(self.pencere)
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya Aç", self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya.addAction(dosya_ac)

        dosya_kaydet = QAction("Dosya Kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")
        dosya.addAction(dosya_kaydet)

        cikis = QAction("Çıkış", self)
        cikis.setShortcut("Ctrl+Q")
        dosya.addAction(cikis)

        ara_degistir = duzenle.addMenu("Ara ve Değiştir")

        ara = QAction("Ara", self)
        ara_degistir.addAction(ara)

        degistir = QAction("Değiştir", self)
        ara_degistir.addAction(degistir)

        temizle = QAction("Temizle", self)
        duzenle.addAction(temizle)

        dosya.triggered.connect(self.response)
        duzenle.triggered.connect(self.duzenle_fonk)

        self.setWindowTitle("Metin Editörü")
        self.show()

    def response(self, action):
        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()
        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()
        elif action.text() == "Çıkış":
            qApp.quit()
    def duzenle_fonk(self,action):
        if action.text()=="Temizle":
            self.pencere.yaziyi_temizle()
        else:
            print(action.text)

app = QApplication(sys.argv)
menu=Menu()
sys.exit(app.exec())