"""
Programa que gera uma calculadora simples

Este programa gera uma calculadora usando a biblioteca pyqt5 que está instalada no próprio ambiente virtual .env
Este é um programa simples, criado apenas para demonstração e futuras consultas.

Modulos Importados:

    sys: É uma bibliteca que coleta e interage com informações do sistema.
        Esta sendo usada para coletar os inputs do usuário para o Pyqt5

    PyQt5: Biblioteca responsável por criar a calculadora.
        Está sendo usada para criar o display que irá exibir os gráficos gerados pela class Calculadora e coletar os inputs.

    main: É o módulo que contém a class e todos os métodos importados do PyQt5 que irão gerar a calculadora.
"""
import sys
from PyQt5.QtWidgets import QApplication
from main import Calculadora

qt = QApplication(sys.argv)
calc = Calculadora()
calc.show()
qt.exec_()
