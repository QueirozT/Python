print('====== Exercício 22 ======')
print()

nome = input('Digite o seu nome: ')
print()

print('Analizando seu nome...')
print('Seu nome em maiscula é: {}'.format(nome.upper()))
print('Seu nome em minuscula é: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(''.join(nome.split()))))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome.split()[0],len(nome.split()[0])))