from random import randint
from time import sleep

print('===== EXERCÍCIO #100 =====')
print()

def sortear(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for i in range(5):
        lista.append(randint(1, 10))
        print(f'{lista[i]}, ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!\n')


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista} temos {soma}!\n')


# Programa Principal
valores = list()

sortear(valores)
somaPar(valores)
