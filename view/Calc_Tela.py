from PyQt6.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence

class TelaPrograma(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("view/untitled.ui", self)
        self.show()
        
        self.lcdNumber = QLCDNumber()

        
        self.btn_1.clicked.connect(lambda: self.AddNumber(1))
        self.btn_2.clicked.connect(lambda: self.AddNumber(2))
        self.btn_3.clicked.connect(lambda: self.AddNumber(3))
        self.btn_4.clicked.connect(lambda: self.AddNumber(4))
        self.btn_5.clicked.connect(lambda: self.AddNumber(5))
        self.btn_6.clicked.connect(lambda: self.AddNumber(6))
        self.btn_7.clicked.connect(lambda: self.AddNumber(7))
        self.btn_8.clicked.connect(lambda: self.AddNumber(8))
        self.btn_9.clicked.connect(lambda: self.AddNumber(9))
        

    def AddNumber(self, numero):
        lastNumber = self.lcdNumber.display(numero)
        if lastNumber == '0':
            result = str(numero)
        else:
            result = lastNumber + str(numero)
        self.lcdNumber.display(result)
            
        
        
        
    def cleanDisplay(self):
        self.lcdNumber.display("0")


