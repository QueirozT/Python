print('===== EXERCÍCIO #42 =====')
print()

print('-=-' * 20)
print('{:^60}'.format('ANALIZADOR DE TRIÂNGULOS'))
print('-=-' * 20)
print()

v01 = float(input('Insira o valor da primeira reta: '))
v02 = float(input('Insira o valor da segunda reta: '))
v03 = float(input('Insira o valor da terceira reta: '))
print()

if (v01 + v02) > v03 and (v01 + v03) > v02 and (v02 + v03) > v01:
    print('Pode-se formar um triângulo com os valores fornecidos.')
    
    if v01 == v02 and v01 == v03:
        print('E o tipo de triângulo é: EQUILÁTERO')
        print()
    elif v01 == v02 or v01 == v03 or v02 == v03:
        print('E o tipo de triângulo é: ISÓSCELES')
        print()
    else:
        print('E o tipo de triângulo é: ESCALENO')
        print()
else:
    print('Não é possível formar um triângulo com os valores fornecidos.')
    print()
