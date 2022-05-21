print('===== EXERCÍCIO #087 =====')
print()

matriz = [[], [], []]
somPar = 0

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Digite um valor para: [ {l} ] [ {c} ]: ')))
    print()

print('~' * 21)

for l in matriz:
    for c in l:
        print(f'[{c:^5}]', end='')
        if c % 2 == 0:
            somPar += c
    print()
print('~' * 21)
print()

print(f'A soma dos valores pares é: {somPar}')
print()

print(f'A soma dos valores da 3ª coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print()

print(f'O maior valor da segunda linha é: {max(matriz[1])}')
print()
