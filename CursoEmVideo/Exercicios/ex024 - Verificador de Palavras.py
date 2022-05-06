print('===== Exercício 24 =====')
print()

texto = str(input('Digite o nome da sua cidade: ')).strip()
print()

verificador = texto.split()

if 'SANTO' in verificador[0].upper():
    print('O nome da sua cidade é: {} \nEla começa com SANTO.'.format(texto))
else:
    print('O nome da sua cidade é: {} \nEla não começa com SANTO.'.format(texto))
print()

# RESULTADOS ALTERNATIVOS:

# print('Contem SANTO? {}'.format('SANTO' in texto.upper()))

# print('Contem SANTO? {}'.format(texto[:5].upper() == 'SANTO'))