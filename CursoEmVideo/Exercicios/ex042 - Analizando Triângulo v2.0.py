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
    
    if v01 == v02 == v03: # O python permite comparações múltiplas entre variáveis.
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


# elif v01 != v02 != v03 != v01:
    # print('O tipo de triângulo é ESCALENO') 

# Diferente de comparações multiplas "iguais", quando utilizo "!=", o python compara individualmente o valor com o posterior. então no caso de 3 ou mais variáveis, temos que informar o valor de todas as variáveis para que possam ser comparadas. no exemplo a cima foi comparado 1 e 2, 2 com 3 e 3 com 1 para fechar o ciclo.
