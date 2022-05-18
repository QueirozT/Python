print('===== EXERCÍCIO #70 =====')
print()

print('==' * 20)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('==' * 20)
print()

tot = caro = barato = 0
rotulo = ''

while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço: R$ '))
    print()

    tot += preco

    if preco > 1000:
        caro += 1
    if barato == 0:
        barato = preco
        rotulo = nome
    elif preco < barato:
        barato = preco
        rotulo = nome

    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

print('~~' * 30)
print('{:^60}'.format(' RESUMO DO DIA '))
print()

print('{:^60}'.format(f'O total da compra foi R${tot:.2f}'))
print('{:^60}'.format(f'Temos {caro} produtos custando mais de R$1000,00'))
print('{:^60}'.format(f'O produto mais barato foi {rotulo} que custa R${barato:.2f}'))
print('~~' * 30)
print()
