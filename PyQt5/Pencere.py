import sys
from PyQt5 import QtWidgets,QtGui
import time
def Pencere(x=100,y=100):
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders1")
    etiket1=QtWidgets.QLabel(pencere)
    etiket1.setText("Burası bir yazıdır.")
    etiket1.move(200,30)
    etiket2=QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("python.png"))
    etiket2.move(120,100)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec())
Pencere()



