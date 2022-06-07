# from math import hypot

print('===== EXERCÍCIO 017 =====')
print()

cop = float(input('Digite o comprimento do cateto oposto: '))
cad = float(input('Digite o comprimento do cateto adjacente: '))
print()

print('A hipotenusa é {:.2f}'.format((cop ** 2 + cad ** 2) ** (1/2)))

# print('A hipotenusa é {:.2f}'.format(hypot(cop, cad)))