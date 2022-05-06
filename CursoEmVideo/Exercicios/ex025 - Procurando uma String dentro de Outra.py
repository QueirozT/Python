print('===== Exercício 25 =====')
print()

nome = str(input('Digite o seu nome: ')).strip()
print()

if 'SILVA' in nome.upper():
    print('O nome "{}" contém a palavra "Silva"'.format(nome))
else:
    print('O nome "{}" não contém a palavra "Silva"'.format(nome))
    print()


# RESULTADO ALTERNATIVO:

# print('Contem Silva? {}'.format('SILVA' in nome.upper()))