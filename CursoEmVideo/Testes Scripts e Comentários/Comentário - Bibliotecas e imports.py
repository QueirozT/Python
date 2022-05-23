# Os Módulos ou Bibliotecas servem para adicionar funcionalidades extras ao Python. 
# Para adicionar uma biblioteca ou módulo ao Python, é necessário instalá-lo no sistema utilizando o comando "pip install nome".

# import biblioteca - Usado para importar uma biblioteca e utilizar seus comandos.
# from biblioteca import comando - Usado para importar comandos específicos de bibliotecas.
# import pygame as pg - Em alguns casos de bibliotecas da comnidade, é necessário utilizar um apelido para elas ex: "as" = "vulgo".

# Para visualizar algumas bibliotecas do python pre-instaladas, basta digitar 'import' e apertar o atalho de visualização "ctrl + space"
# Uma lista com todas as bibliotecas de python pode ser vista em Pypi: https://pypi.org

# Ex:

# - BIBLIOTECA RANDOM: utilizada para gerar números aleatórios ou re-ordenar itens.

# import random

# random.randint(1, 10) #Retorna um número aleatório entre 1 e 10.
# random.choice(['a', 'b', 'c']) #Retorna um item aleatório de uma lista.
# random.shuffle(['a', 'b', 'c']) #Re-ordena itens de uma lista.
# random.sample(['a', 'b', 'c'], valor) #Retorna uma lista com o "valor" de itens aleatórios de uma lista.
# random.random() #Retorna um número aleatório entre 0 e 1.
# random.seed() #Inicializa e ou define a semente para o processo de randomização. ps: não é necessário chamar.

# - BIBLIOTECA MATH: utilizada para realizar operações matemáticas.

# import math

# math.ceil(valor) #Arredonda para cima.
# math.floor(valor) #Arredonda para baixo.
# math.fabs(valor) #Retorna o valor absoluto.
# math.factorial(valor) #Retorna o fatorial de um número.
# math.fsum(lista) #Retorna a soma de todos os itens de uma lista.
# math.gcd(valor1, valor2) #Retorna o máximo divisor comum.
# math.isclose(valor1, valor2, valor3) #Retorna True se os valores são "aproximadamente" iguais.
# math.isinf(valor) #Retorna True se o valor é infinito.
# math.isnan(valor) #Retorna True se o valor é NaN (Not a Number).
# math.log(valor, base) #Retorna o logaritmo de um número.
# math.modf(valor) #Retorna um tuplo com o valor inteiro e o resto da divisão.
# math.pow(valor1, valor2) #Retorna o valor de valor1 elevado a valor2.
# math.sqrt(valor) #Retorna a raiz quadrada de um número.
# math.trunc(valor) #Arredonda para baixo.


# - BIBLIOTECA TIME: utilizada para realizar operações de tempo.

# import time

# time.time() #Retorna o tempo atual em segundos.
# time.localtime() #Retorna um tuplo com as informações de tempo.
# time.strftime('%H:%M:%S') #Retorna uma string com o horário atual.
# time.sleep(valor) #Pausa o programa por "valor" segundos.
# time.perf_counter() #Retorna o tempo atual em segundos.
# time.perf_frequency() #Retorna a frequência de atualização do relógio do sistema.


# - BIBLIOTECA DATETIME: utilizada para realizar operações de data e hora.

# from datetime import datetime # Importa o módulo "datetime".

# datetime.now() #Retorna a data e hora atual.
# datetime.today() #Retorna a data atual.
# datetime.fromtimestamp(valor) #Retorna a data e hora a partir de um valor de tempo.
# datetime.utcfromtimestamp(valor) #Retorna a data e hora a partir de um valor de tempo em UTC.
# datetime.strptime(valor, '%d/%m/%Y') #Retorna a data e hora a partir de uma string.
# datetime.strftime(valor, '%d/%m/%Y') #Retorna uma string a partir de uma data e hora.
# datetime.combine(data, hora) #Retorna uma data e hora a partir de uma data e hora.
# datetime.date(valor) #Retorna a data a partir de uma data e hora.
# datetime.time(valor) #Retorna a hora a partir de uma data e hora.
# datetime.weekday(valor) #Retorna o dia da semana a partir de uma data e hora.
# datetime.isoweekday(valor) #Retorna o dia da semana a partir de uma data e hora.
# datetime.isocalendar(valor) #Retorna o dia da semana a partir de uma data e hora.
# datetime.isoformat(valor) #Retorna uma string a partir de uma data e hora.
# datetime.fromordinal(valor) #Retorna uma data a partir de um número de dia.


# - BIBLIOTECA OPERATOR: utilizada para realizar operações de strings. (CONSULTAR COMENTÁRIO DE VARIÁVEIS COMPOSTAS)

# from operator import itemgetter, attrgetter, methodcaller # Importa os módulos "itemgetter", "attrgetter" e "methodcaller".

# itemgetter(valor) #Retorna um método que retorna um item de uma lista.
# attrgetter(valor) #Retorna um método que retorna um atributo de uma lista.
# methodcaller(valor) #Retorna um método que chama um método de uma lista.
