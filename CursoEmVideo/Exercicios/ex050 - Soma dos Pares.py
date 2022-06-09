print('===== EXERCÍCIO #50 =====')
print()

soma = 0
contador = 0

for i in range(1, 7):
    numero = int(input('Digite o {}° valor: '.format(i)))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print()

print('A soma dos {} números pares é {}'.format(contador, soma))
print()
