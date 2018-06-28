import sys
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.radio_label=QLabel("Hangi dili daha çok seviyorsun?")
        self.java=QRadioButton("Java")
        self.python=QRadioButton("Python")
        self.php=QRadioButton("PHP")
        self.label=QLabel("")
        self.buton=QPushButton("Gönder")
        v_box=QVBoxLayout()
        v_box.addWidget(self.radio_label)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.label)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.setWindowTitle("Radio Button")
        self.show()
        self.buton.clicked.connect(lambda : self.click(self.java.isChecked(),self.python.isChecked(),self.php.isChecked(),self.label))
    def click(self,java,python,php,label):
        if java: label.setText("Java")
        if python: label.setText("Python")
        if php: label.setText("PHP")
app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec())