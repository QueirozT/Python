print('===== EXERCÍCIO #48 =====')
print()

contagem = 0
soma = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        contagem += i
        soma += 1

print('A soma de todos os {} valores impares múltiplos de 3 entre 1 e 500 é: {}'.format(soma, contagem))
print()
