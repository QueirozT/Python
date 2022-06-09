from math import radians, sin, cos, tan

print('===== EXERCÍCIO 018 =====')
print()

angulo = float(input('Digite o ângulo que você deseja: '))
print()

seno = sin(radians(angulo))
print('O seno de {} é {:.2f}'.format(angulo, seno))
print()

cosseno = cos(radians(angulo))
print('O cosseno de {} é {:.2f}'.format(angulo, cosseno))
print()

tangente = tan(radians(angulo))
print('A tangente de {} é {:.2f}'.format(angulo, tangente))
print()
