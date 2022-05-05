from random import choice

print('===== EXERCÍCIO 019 =====')
print()

item01 = input('Digite o primeiro nome: ')
item02 = input('Digite o segundo nome: ')
item03 = input('Digite o terceiro nome: ')
item04 = input('Digite o quarto nome: ')
print()

lista = [item01, item02, item03, item04]
escolha = choice(lista)

print('O nome escolhido foi {}.'.format(escolha))
