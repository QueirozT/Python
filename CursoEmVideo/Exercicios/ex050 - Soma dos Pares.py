print('===== EXERCÍCIO #50 =====')
print()

soma = 0

for i in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
print()

print('A soma dos números pares é: {}'.format(soma))
print()
