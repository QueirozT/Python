import sys
from PyQt5.QtWidgets import QApplication
from main import Calculadora

qt = QApplication(sys.argv)
calc = Calculadora()
calc.show()
qt.exec_()
