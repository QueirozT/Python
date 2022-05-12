print('===== EXERCÍCIO #48 =====')
print()

contagem = 0

for i in range(1, 501):
    if i % 3 == 0:
        contagem += i

print('A soma dos valores impares múltiplos de 3 entre 1 e 500 é: {}'.format(contagem))
print()
