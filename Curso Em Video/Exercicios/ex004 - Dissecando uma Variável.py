print('===== EXERCÍCIO 004 =====')
print()

valor = input('Digite Algo: ')
print()

print('O tipo primitivo desse valor é: {}'.format(type(valor)))
print('Só contém espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas?', valor.islower())
print('Está capitalizada?', valor.istitle())
