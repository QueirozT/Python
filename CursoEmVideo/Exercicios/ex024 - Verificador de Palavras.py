print('===== Exercício 24 =====')
print()

texto = input('Digite o nome da sua cidade: ')
print()

verificador = texto.split()

if 'SANTO' in verificador[0].upper():
    print('O nome da sua cidade é: {} \nEla começa com SANTO.'.format(texto))
else:
    print('O nome da sua cidade é: {} \nEla não começa com SANTO.'.format(texto))
print()