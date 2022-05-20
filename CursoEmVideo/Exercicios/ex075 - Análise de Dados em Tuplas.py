print('===== EXERCÍCIO #075 =====')
print()

tupla = ()

for i in range(4):
    tupla += (int(input('Digite um Número: ')),)
print()

print(f'Você digitou os valores: {tupla}')
print()

if tupla.count(9) > 0:
    print(f'O valor 9 aparece {tupla.count(9)} vez(es).')
else:
    print('O valor 9 não foi digitado.')
print()

if tupla.count(3) > 0:
    print(f'O valor 3 foi encontrado na posição {tupla.index(3)}.')
else:
    print('O valor 3 não foi digitado.')
print()

print('Os números pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
print('\n')
