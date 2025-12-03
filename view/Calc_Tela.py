from PyQt5.QtWidgets import QLCDNumber, QApplication, QMainWindow
from PyQt5.uic import loadUi
from funcoes import sum, sub, multiplicar, div, percent

class TelaPrograma(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("view/untitled.ui", self)
        self.show()

        self.current_value = ""
        self.last_value = ""
        self.operation = None

        self.btn_0.clicked.connect(lambda: self.add_digito("0"))
        self.btn_1.clicked.connect(lambda: self.add_digito("1"))
        self.btn_2.clicked.connect(lambda: self.add_digito("2"))
        self.btn_3.clicked.connect(lambda: self.add_digito("3"))
        self.btn_4.clicked.connect(lambda: self.add_digito("4"))
        self.btn_5.clicked.connect(lambda: self.add_digito("5"))
        self.btn_6.clicked.connect(lambda: self.add_digito("6"))
        self.btn_7.clicked.connect(lambda: self.add_digito("7"))
        self.btn_8.clicked.connect(lambda: self.add_digito("8"))
        self.btn_9.clicked.connect(lambda: self.add_digito("9"))

        self.btn_add.clicked.connect(lambda: self.set_operation("+"))
        self.btn_sub.clicked.connect(lambda: self.set_operation("-"))
        self.btn_mul.clicked.connect(lambda: self.set_operation("*"))
        self.btn_div.clicked.connect(lambda: self.set_operation("/"))
        self.btn_percentage.clicked.connect(lambda: self.set_operation("%"))

        self.btn_equal.clicked.connect(self.equals)
        self.btn_clear.clicked.connect(self.clear_all)
        self.btn_comma.clicked.connect(self.add_comma)
        self.btn_back.clicked.connect(self.backspace)
        self.btn_inv.clicked.connect(self.reverses_value)
        

    def atualizar_display(self):
        if self.current_value == "":
            self.lcdMain.display("0")
        else:
            self.lcdMain.display(self.current_value)

    def atualizar_historico(self):
        if self.last_value and self.operation:
            self.lcdHistory.display(f"{self.last_value} {self.operation}")
        else:
            self.lcdHistory.display("")

    def add_digito(self, digit):
        if self.current_value == "0":
            self.current_value = digit
        else:
            self.current_value += digit
        self.atualizar_display()

    def reverses_value(self):
        if self.current_value:
            number = str(float(self.current_value.replace(",", ".")) * -1).replace(".", ",")
            self.current_value = number
            self.atualizar_display()

    def add_comma(self):
        if "," not in self.current_value:
            if self.current_value == "":
                self.current_value = "0,"
            else:
                self.current_value += ","
        self.atualizar_display()

    def backspace(self):
        self.current_value = self.current_value[:-1]
        self.atualizar_display()

    def clear_all(self):
        self.current_value = ""
        self.last_value = ""
        self.operation = None
        self.atualizar_display()
        self.atualizar_historico()

    def set_operation(self, op):
        if self.current_value == "":
            return
        self.last_value = self.current_value.replace(",", ".")
        self.current_value = ""
        self.operation = op
        self.atualizar_historico()
        self.atualizar_display()

    def equals(self):
        if not self.operation or self.current_value == "":
            return

        num1 = float(self.last_value)
        num2 = float(self.current_value.replace(",", "."))

        if self.operation == "+":
            result = sum(num1, num2)
        elif self.operation == "%":
            result = percent(num1, num2)
        elif self.operation == "-":
            result = sub(num1, num2)
        elif self.operation == "*":
            result = multiplicar(num1, num2)
        elif self.operation == "/":
            result = div(num1, num2)
            if result == "Erro na divisão":
                self.lcdMain.display("Erro")
                return
        else:
            return

        self.lcdHistory.display(f"{num1} {self.operation} {num2}")
        self.last_value = ""
        self.operation = None
        self.current_value = str(result).replace(".", ",")
        self.atualizar_display()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = TelaPrograma()
    sys.exit(app.exec_())
