print('===== EXERCÍCIO #60 =====')
print()

valor = int(input('Digite um valor: '))
print()

c = valor # O contador começa com o valor digitado

fatorial = 1 # Preciso inicializar em 1 pois qualquer valor * 0 é 0, e * 1 é o próprio número.

while c != 0:
    fatorial *= c
    c -= 1 # O contador é decrementado a cada iteração até chegar no valor 0

print('O fatorial de {} é {}'.format(valor, fatorial))
print()



# PROGRAMA ALTERNATIVO:

# from math import factorial
# print()

# n = int(input('Digite um número: '))
# f = factorial(n)

# print('O fatorial de {} é {}'.format(n, f))
# print()



# PROGRAMA ALTERNATIVO 2:

# n = int(input('Digite um número para calcular seu fatorial: '))
# print()

# c = n
# f = 1

# print('Calculando {}! = '.format(n), end='')

# while c > 0:
#     print('{}'.format(c), end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1

# print('{}'.format(f))
# print()
