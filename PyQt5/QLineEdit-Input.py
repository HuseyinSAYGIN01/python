import sys
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Yaz Temizle")
        self.yazı_alanı=QtWidgets.QLineEdit()
        self.temizle=QtWidgets.QPushButton("Temizle")
        self.yazdır=QtWidgets.QPushButton("Yazdır")
        self.label=QtWidgets.QLabel("")
        self.solasil=QtWidgets.QPushButton("Sola Sil")
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addWidget(self.solasil)
        v_box.addWidget(self.label)
        v_box.addStretch()
        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.show()
        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)
        self.solasil.clicked.connect(self.click)
    def click(self):
        sender=self.sender()
        if sender.text()=="Temizle":
            self.yazı_alanı.clear()
        elif sender.text()=="Sola Sil":
            self.yazı_alanı.setText(self.yazı_alanı.text()[:-1])
        else:
            self.label.setText(self.yazı_alanı.text())
            self.yazı_alanı.clear()


app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec())