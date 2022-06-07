print('===== EXERCÍCIO #078 =====')
print()

lista = []

for i in range(5):
    lista.append(int(input(f'Digite um valor para a posição {i} da lista: ')))

print()
print(f'Você digitou os valores {lista}.')
print()

print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for p, i in enumerate(lista):
    if i == max(lista):
        print(f'{p}...', end='')
print('\n')

print(f'O menor valor digitado foi {min(lista)} nas posições ', end='')
for p, i in enumerate(lista):
    if i == min(lista):
        print(f'{p}...', end='')
print('\n')
