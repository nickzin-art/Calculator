from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QApplication, QMainWindow
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
        

class Calculadora(QMainWindow):
    
    def addNumber(self, number):
        numberDisplay1 = self.display.setText(number)
        self.display_2.setText(numberDisplay1)
        
        
    def cleanDisplay(self):
        self.display.setText("0")
        
    def setOperation(self):
        result = self.display.text()
        self.display_2.setText(result)
        
    def getNumberDisplay(self, display):
        num = display.text()
        if "," in num1:
            num1 = num1.replace(',', '.')
            num1 = float(num1)
        num1 = int(num1) 
        
    def setNumberDisplay(self, number):
        number = str(number)
        number = number.replace('.', ',')
        self.display.setText(number)
        
    def showResult(self):
        num1 = self.getNumberDisplay(self.display)
        num2 = self.getNumberDisplay(self.display_2)
        
        result = sum(num1, num2)
        self.setNumberDisplay(result)
        
    def addComma(self):
        last = self.display.text()
        if last.count(",") > 0:
            result = last
        else:
            result = last + ","
        self.display.setText(result)
        
    


