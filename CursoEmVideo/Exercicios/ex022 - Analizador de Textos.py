print('====== Exercício 22 ======')
print()

nome = input('Digite o seu nome: ')
print()

print('O nome digitado em maiscula é: {}'.format(nome.upper()))
print()

print('O nome digitado em minuscula é: {}'.format(nome.lower()))
print()

novoNome = nome.split()
print('A quantidade de letras do nome é: ', len(''.join(novoNome)))
print()

print('Apenas o primeiro nome tem {} letras.'.format(len(novoNome[0])))