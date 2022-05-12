print('===== EXERCÍCIO #45 =====')
print()

print('{:^80}'.format('ESCOLHA UMA DAS OPÇÕES PARA CRIAR A TABUADA!!!'))
print('-=' * 40)
print('{:^80}'.format('[ 1 ] - ADIÇÃO | [ 2 ] - SUBTRAÇÃO | [ 3 ] - MULTIPLICAÇÃO | [ 4 ] - DIVISÃO'))
print('-=' * 40)
print()

opcao = int(input('Escolha uma das opções para calcular: '))
print()

valor = int(input('Digite um número: '))
print()

if opcao == 1:
    print('{:^22}'.format('TABUADA DE ADIÇÃO:'))
    for i in range(1, 11):
        print('{:^22}'.format('{}  +  {:<3}  =  {}'.format(valor, i, valor + i)))
    print()
elif opcao == 2:
    print('{:^22}'.format('TABUADA DE SUBTRAÇÃO:'))
    for i in range(1, 11):
        print('{:^22}'.format('{}  -  {:<3}  =  {}'.format(valor, i, valor - i)))
    print()
elif opcao == 3:
    print('{:^22}'.format('TABUADA DE MULTIPLICAÇÃO:'))
    for i in range(1, 11):
        print('{:^22}'.format('{}  x  {:<3}  =  {}'.format(valor, i, valor * i)))
    print()
elif opcao == 4:
    print('{:^22}'.format('TABUADA DE DIVISÃO:'))
    for i in range(1, 11):
        print('{:^22}'.format('{}  /  {:<3}  =  {:<10.1f}'.format(valor, i, valor / i)))
    print()
else:
    print('Opção inválida!')
    print()
    