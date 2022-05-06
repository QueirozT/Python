print('===== Exercício 27 =====')
print()

nome = input('Digite o seu nome: ')
print()

print('O nome digitado foi: {}'.format(nome))
print()

print('O primeiro nome é: {}'.format(nome.split()[0]))
print()

print('O último nome é: {}'.format(nome.split()[-1]))
print()


# Resultado Alternativo:

# print('O primeiro nome é: {}'.format(nome.split()[0]))
# print()
# print('O último nome é: {}'.format(nome.split()[len(nome.split()) - 1]))
# print()

