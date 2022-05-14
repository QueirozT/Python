print('===== EXERCÍCIO #60 =====')
print()

valor = int(input('Digite um valor: '))
print()

c = valor

fatorial = 1

while c != 0:
    fatorial = fatorial * c
    c -= 1

print('O fatorial de {} é {}'.format(valor, fatorial))
print()
