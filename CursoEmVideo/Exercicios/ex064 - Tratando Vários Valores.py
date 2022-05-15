print('===== EXERCÍCIO #64 =====')
print()

print('Iniciando...')
print()

print('Para parar a leitura, insira 999 no campo de valor.')
print()

soma = 0
valor = 0

while valor != 999:
    valor = int(input('Qual o valor? '))
    if valor != 999:
        soma += valor
    print()
print('Finalizando...')
print()

print('A soma de todos os valores digitados é {}.'.format(soma))
print()
