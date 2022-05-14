print('===== EXERCÍCIO #59 =====')
print()

opcao = ''

v01 = float(input('Digite o primeiro valor: '))
v02 = float(input('Digite o segundo valor: '))
print()

while opcao != 5:
    print('-=' * 11)
    print('{:^22}'.format(' MENU '))
    print('-=' * 11)
    print('{}'.format('[ 1 ] SOMAR'))
    print('{}'.format('[ 2 ] MULTIPLICAR'))
    print('{}'.format('[ 3 ] MAIOR'))
    print('{}'.format('[ 4 ] NOVOS NÚMEROS'))
    print('{}'.format('[ 5 ] SAIR DO PROGRAMA'))
    print()
    opcao = int(input('Escolha uma opção! '))
    print()
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(v01, v02, v01 + v02))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}'.format(v01, v02, v01 * v02))
    elif opcao == 3:
        if v01 > v02:
            print('{} é maior que {}'.format(v01, v02))
        else:
            print('{} é maior que {}'.format(v02, v01))
    elif opcao == 4:
        v01 = float(input('Digite o primeiro valor: '))
        v02 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
    print()
