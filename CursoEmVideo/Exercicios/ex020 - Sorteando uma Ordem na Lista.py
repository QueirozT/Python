from random import shuffle

print('===== EXERCÍCIO 020 =====')
print()

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
print()

lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem de apresentação será:')
print(lista)
