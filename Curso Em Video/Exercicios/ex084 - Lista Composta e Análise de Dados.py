print('===== EXERCÍCIO #084 =====')
print()

lista = list()
mais = menos = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))

    lista.append([nome, peso])

    if len(lista) == 1:
        mais = menos = peso
    else:
        if peso > mais:
            mais = peso
        if peso < menos:
            menos = peso

    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    print()

    if opcao == 'N':
        break

print('~~' * 20)
print(f'Ao todo você cadastrou {len(lista)} pessoas.')

print(f'O maior peso registrado foi {mais}kg de:', end='')
for p in lista:
    if p[1] == mais:
        print(f' {p[0]}', end='.')
print('')

print(f'O menor peso registrado foi {menos}kg de:', end='')
for p in lista:
    if p[1] == menos:
        print(f' {p[0]}', end='.')
print('\n')
