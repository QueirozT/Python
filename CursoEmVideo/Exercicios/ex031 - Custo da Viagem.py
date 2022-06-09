print('===== EXERCÍCIO 31 =====')
print()

valor = input('Qual a distância da viagem em km? ')
print()

if valor.isnumeric():
    valor = float(valor)

    if valor >= 200:
        print('A sua passagem custará R${:.2f}'.format(valor * 0.45))
        print()
    else:
        print('A sua passagem custará R${:.2f}'.format(valor * 0.50))
        print()
else:
    print('"{}" é um valor inválido!'.format(valor))
    print()

# Resultado Alternativo:

# preco = valor * 0.50 if valor <= 200 else valor * 0.45
# print('A sua passagem custará R${:.2f}'.format(preco))