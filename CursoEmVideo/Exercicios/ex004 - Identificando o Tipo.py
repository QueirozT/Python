print('===== EXERCÍCIO 004 =====')
print()

valor = input('Digite um valor: ')
print()

print('O tipo primitivo desse valor é: {}'.format(type(valor)))
print()

print('Só contém espaços? {}'.format(valor.isspace()))
print()

print('É um número? {}'.format(valor.isnumeric()))
print()

print('É alfabético? {}'.format(valor.isalpha()))
print()

print('É alfanumérico? {}'.format(valor.isalnum()))
print()

print('Está em maiúsculas? {}'.format(valor.isupper()))
print()

print('Está em minúsculas? {}'.format(valor.islower()))
print()

print('Está capitalizada? {}'.format(valor.istitle()))
print()
