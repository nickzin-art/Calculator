from PyQt5.QtWidgets import QApplication
from view.Calc_Tela import TelaPrograma

if __name__ == "__main__":
    app = QApplication([])

    tela = TelaPrograma()
    app.exec_()
    

      