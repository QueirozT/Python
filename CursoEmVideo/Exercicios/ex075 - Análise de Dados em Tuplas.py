print('===== EXERCÍCIO #075 =====')
print()

tupla = ()

for i in range(4):
    tupla += (int(input('Digite um Número: ')),)
print()

print(f'Você digitou os valores: {tupla}')
print()

if tupla.count(9) > 0: # Verifica se existe o número 9 dentro da tupla.
    print(f'O valor 9 aparece {tupla.count(9)} vez(es).')
else:
    print('O valor 9 não foi digitado.')
print()

if 3 in tupla: # Usando o in para procurar um valor dentro da tupla.
    print(f'O valor 3 foi encontrado na {tupla.index(3)+1}º posição.')
else:
    print('O valor 3 não foi digitado.')
print()

print('Os números pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
print('\n')
