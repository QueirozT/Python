print('===== EXERCÍCIO 015 =====')
print()

km = float(input('Qual a distância percorrida em Km? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
print()

print('O valor a ser pago é de R${:.2f}'.format((km * 0.15) + (dias * 60)))
