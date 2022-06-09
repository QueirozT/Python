print('===== EXERCÍCIO #61 =====')
print()

print('=-' * 20)
print('{:^40}'.format('PROGRESSÃO ARITMÉTICA'))
print('=-' * 20)
print()

valor = int(input('Qual o número? '))
r = int(input('Qual a razão? '))
print()

c = 10

while c != 0:
    print('{}'.format(valor), end=" -> ")
    valor += r
    c -= 1
print('FIM!')
print()
