print('===== EXERCÍCIO 35 =====')
print()

print('-=-' * 20)
print('{:^60}'.format('Analizador de Triângulos'))
print('-=-' * 20)
print()

v01 = float(input('Qual o comprimento da primeira reta? '))
v02 = float(input('Qual o comprimento da segunda reta? '))
v03 = float(input('Qual o comprimento da terceira reta? '))
print()

if (v01 + v02) > v03 and (v01 + v03) > v02 and (v02 + v03) > v01:
    print('Um triângulo pode ser feito com as medidas fornecidas.')
    print()
else:
    print('Não é possível fazer um triângulo com estas medidas.')
    print()
