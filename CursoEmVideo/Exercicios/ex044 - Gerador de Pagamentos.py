print('===== EXERCÍCIO #44 =====')
print()

valor = float(input('Insira o valor do produto: R$'))
print()

# Utilizando o print com áspas triplas para formatação literal.
print('''FORMAS DE PAGAMENTO
[ 1 ] - À VISTA (DINHEIRO/PIX)
[ 2 ] - À VISTA (CARTÃO)
[ 3 ] - 2X (CARTÃO)
[ 4 ] - 3X OU MAIS (CARTÃO)
''')

pagamento = int(input('Qual a forma de pagamento? '))
print()

if pagamento == 1:
    print('Sua compra de R${:.2f} com o desconto de 10% vai custar R${:.2f}'.format(valor, valor - (valor * 0.1)))
    print()
elif pagamento == 2:
    print('Sua compra de R${:.2f} com o desconto de 5% vai custar R${:.2f}'.format(valor, valor - (valor * 0.05)))
    print()
elif pagamento == 3:
    print('Sua compra será parcelada em 2X de R${:.2f}'.format(valor / 2))
    print('Sua compra ao final irá custar R${:.2f}'.format(valor))
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
