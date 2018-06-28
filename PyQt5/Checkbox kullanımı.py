import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.check=QCheckBox("Python'ı seviyor musunuz?")
        self.label=QLabel("")
        self.buton=QPushButton("Bana Tıkla")
        v_box=QVBoxLayout()
        v_box.addWidget(self.check)
        v_box.addWidget(self.label)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.show()
        self.buton.clicked.connect(lambda : self.label.setText("Evet") if self.check.isChecked() else self.label.setText("Hayır"))
"""
    def click(self):
        if self.check.isChecked():
            self.label.setText("Evet")
        else:
            self.label.setText("Hayır")
"""
app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec())