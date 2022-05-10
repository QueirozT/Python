print('===== EXERCÍCIO #44 =====')
print()

valor = float(input('Insira o valor do produto: R$'))
print()

print('ESCOLHA A FORMA DE PAGAMENTO:')
print('1 - À VISTA (DINHEIRO/CHEQUE) - 10% de desconto')
print('2 - À VISTA (CARTÃO) - 5% de desconto')
print('3 - EM ATÉ 2x (CARTÃO) - valor normal')
print('4 - ACIMA DE 3X (CARTÃO) - 20% de juros')
print()
pagamento = int(input('Qual a forma de pagamento? '))
print()

if pagamento == 1:
    print('O valor do produto com o desconto é: R${:.2f}'.format(valor - (valor * 0.1)))
    print()
elif pagamento == 2:
    print('O valor do produto com o desconto é: R${:.2f}'.format(valor - (valor * 0.05)))
    print()
elif pagamento == 3:
    print('O valor do produto é R${:.2f}'.format(valor))
    print()
elif pagamento == 4:
    print('O valor do produto com o juros é: R${:.2f}'.format(valor + (valor * 0.2)))
    print()
else:
    print('Opção inválida!')
    print()
