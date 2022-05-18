print('===== EXERCÍCIO #67 =====')
print()

print('~~' * 23)
print('{:^46}'.format('GERADOR DE TABUADA DE MULTIPLICAÇÃO'))
print('{:^46}'.format('PARA FINALIZAR DIGITE UM VALOR NEGATIVO!'))
print('~~' * 23)
print()

while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    print()

    if num <= 0:
        break

    print('{:^20}'.format(f'Tabuada de {num}'))
    print('-' * 20)
    for n in range(1, 11):
        print('{:^20}'.format(f'{num} * {n:^3} = {num * n}'))
    print('-' * 20)

print('FINALIZANDO O PROGRAMA...')
print()
