import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Criando a tela
        self.setWindowTitle('Calculadora Simples')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        # Criando a formatação e o comportamento do layout
        self.display = QLineEdit()
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '*{background: #fff; color: #000; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        
        # Criando o Layout (x, y, largura, altura).
        self.grid.addWidget(self.display, 0, 0, 1, 5)

        # Criando e Adicionando os botões ao layout.
        self.add_btn(QPushButton('7'), 1, 0, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('8'), 1, 1, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('9'), 1, 2, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('+'), 1, 3, 1, 1, style='background: #545251; color: #fff; font-weight: 700; font-size: 20px')
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            'background: #363534; color: #fff; font-weight: 700; font-size: 20px'
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('5'), 2, 1, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('6'), 2, 2, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('-'), 2, 3, 1, 1, style='background: #545251; color: #fff; font-weight: 700; font-size: 20px')
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background: #363534; color: #fff; font-weight: 700; font-size: 20px'
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('2'), 3, 1, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('3'), 3, 2, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('/'), 3, 3, 1, 1, style='background: #545251; color: #fff; font-weight: 700; font-size: 20px')
        self.add_btn(
            QPushButton('='), 3, 4, 2, 1,
            self.eval_igual,
            'background: #095177; color: #fff; font-weight: 700; font-size: 20px'
        )

        self.add_btn(QPushButton('.'), 4, 0, 1, 1, style='font-size: 20px')
        self.add_btn(QPushButton('0'), 4, 1, 1, 2, style='font-size: 20px')
        self.add_btn(QPushButton('*'), 4, 3, 1, 1, style='background: #545251; color: #fff; font-weight: 700; font-size: 20px')

        # Adicionando o layout a tela.
        self.setCentralWidget(self.cw)

    # Função que Cria e Adiciona os botões ao layout.
    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    # Função que valida e executa as expressões.
    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Expressão Inválida.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
