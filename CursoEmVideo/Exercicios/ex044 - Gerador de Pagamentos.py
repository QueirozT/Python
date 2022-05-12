print('===== EXERCÍCIO #44 =====')
print()

valor = float(input('Insira o valor do produto: R$'))
print()

print('ESCOLHA A FORMA DE PAGAMENTO:')
print('[ 1 ] - À VISTA (DINHEIRO/CHEQUE) - 10% de desconto')
print('[ 2 ] - À VISTA (CARTÃO) - 5% de desconto')
print('[ 3 ] - EM ATÉ 2x (CARTÃO) - valor normal')
print('[ 4 ] - A PARTIR DE 3X (CARTÃO) - 20% de juros')
print()
pagamento = int(input('Qual a forma de pagamento? '))
print()

if pagamento == 1:
    print('Sua compra de R${:.2f} com o desconto de 10% vai custar R${:.2f}'.format(valor, valor - (valor * 0.1)))
    print()
elif pagamento == 2:
    print('Sua compra de R${:.2f} com o desconto de 5% vai custar R${:.2f}'.format(valor, valor - (valor * 0.05)))
    print()
elif pagamento == 3:
    print('Sua compra vai custar R${:.2f}'.format(valor))
    print()
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print()

    if parcelas < 3:
        print('Quantidade de parcelas inválida!')
        print()
    else:
        print('Sua compra será parcelada em {}x de R${:.2f}'.format(parcelas, (valor + (valor * 0.2)) / parcelas))
        print('Sua compra de R${:.2f} com os jurus ao final irá custar R${:.2f}'.format(valor, valor + (valor * 0.2)))
        print()
else:
    print('Opção inválida!')
    print()
