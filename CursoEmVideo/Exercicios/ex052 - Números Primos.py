print('====== EXERCÍCIO #52 ======')
print()

numero = int(input('Digite um número: '))

contador = 0
if numero > 1:
    for i in range(1, numero + 1):
        if i != 1 and i != numero:
            if numero % i == 0:
                contador += 1
            else:
                contador += 0
else:
    contador = 1
    
if contador == 0:
    print('O número {} é primo.'.format(numero))
else:
    print('O número {} não é primo.'.format(numero))
print()
