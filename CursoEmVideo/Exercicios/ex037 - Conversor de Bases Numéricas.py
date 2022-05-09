print('===== EXERCÍCIO #37 =====')
print()

valor = int(input('Insira o número que deseja converter: '))
print()

print('Deseja converter para:')
print('Binário: 1')
print('Octal: 2')
print('Hexadecimal: 3')
base = int(input('Digite o valor desejado: '))
print()

if base == 1:
    print('O número {} em binário é: {}'.format(valor, bin(valor)[2:]))
    print()
elif base == 2:
    print('O número {} em octal é: {}'.format(valor, oct(valor)[2:]))
    print()
elif base == 3:
    print('O número {} em hexadecimal é: {}'.format(valor, hex(valor)[2:]))
    print()
else:
    print('Não existe essa opção!')
    print()
