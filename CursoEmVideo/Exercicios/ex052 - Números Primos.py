print('====== EXERCÍCIO #52 ======')
print()

num = int(input('Digite um número: '))
print()

tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}\033[m'.format(c), end=' ')
print('\n')

print('O numero {} foi divisível {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
print()


# VERSÃO ALTERNATIVA DO PROGRAMA:

# numero = int(input('Digite um número: '))

# contador = 0
# if numero > 1:
#     for i in range(1, numero + 1):
#         if i != 1 and i != numero:
#             if numero % i == 0:
#                 contador += 1
#             else:
#                 contador += 0
# else:
#     contador = 1
    
# if contador == 0:
#     print('O número {} é primo.'.format(numero))
# else:
#     print('O número {} não é primo.'.format(numero))
# print()
