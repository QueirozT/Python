print('===== EXERCÍCIO 33 =====')
print()

v01 = int(input('Digite o primeiro valor: '))
v02 = int(input('Digite o segundo valor: '))
v03 = int(input('Digite o terceiro valor: '))
print()

pri = 0
seg = 0
ter = 0

# primeiro valor:
if v01 > v02:
    pri = 'true' 
if v01 < v02:
    pri = 'false' 

# segundo valor:
if v01 > v03:
    seg = 'true' 
if v01 < v03:
    seg = 'false' 

# terceiro valor:
if v02 > v03:
    ter = 'true'
if v02 < v03:
    ter = 'false'

verificador = [pri, seg, ter]


if verificador == ['true', 'true', 'false']:
    print('"{}" é maior que "{}" que também é maior que "{}"!'.format(v01, v03, v02))
    print()
elif verificador == ['true', 'false', 'true']:
    print('"{}" é maior que "{}" que também é maior que "{}"!'.format(v02, v03, v01))
    print()
elif verificador == ['true', 'false', 'false']:
    print('"{}" é maior que "{}" que também é maior que "{}"!'.format(v03, v01, v02))
    print()
elif verificador == ['false', 'true', 'true']:
    print('"{}" é maior que "{}" que também é maior que "{}"!'.format(v02, v01, v03))
    print()
elif verificador == ['false', 'false', 'false']:
    print('"{}" é maior que "{}" que também é maior que "{}"!'.format(v03, v02, v01))
    print()
elif verificador == ['true', 'true', 'true']:
    print('"{}" é maior que "{}" que também é maior que "{}"!'.format(v01, v02, v03))
elif v01 == v02 and v01 > v03:
    print('"{}" é igual a "{}" e é maior que "{}"!'.format(v01, v02, v03))
    print()
elif v01 == v02 and v01 < v03:
    print('"{}" é igual a "{}" e é menor que "{}"!'.format(v01, v02, v03))
    print()
elif v01 == v03 and v01 > v02:
    print('"{}" é igual a "{}" e é maior que "{}"!'.format(v01, v03, v02))
    print()
elif v01 == v03 and v01 < v02:
    print('"{}" é igual a "{}" e é menor que "{}"!'.format(v01, v03, v02))
    print()
elif v02 == v03 and v02 > v01:
    print('"{}" é igual a "{}" e é maior que "{}"!'.format(v02, v03, v01))
    print()
elif v02 == v03 and v02 < v01:
    print('"{}" é igual a "{}" e é menor que "{}"!'.format(v02, v03, v01))
    print()
else:
    print('Os valores são iguais!')
    print()



# SEGUNDA VERSÃO CRIADA (SIMPLIFICADA E USADA NA ÁULA):

# maior = v01
# if v02 > v01 and v02 > v03:
#     maior = v02
# if v03 > v01 and v03 > v02:
#     maior = v03
# menor = v01
# if v02 < v01 and v02 < v03:
#     menor = v02
# if v03 < v01 and v03 < v02:
#     menor = v03
# print('O maior valor é {} e o menor valor é {}!'.format(maior, menor))
# print()



# PRIMEIRA VERSÃO CRIADA (PARCIALMENTE FUNCIONAL).

# if v01.isnumeric() and v02.isnumeric() and v03.isnumeric():
#     v01 = int(v01)
#     v02 = int(v02)
#     v03 = int(v03)

#     if v01 > v02 and v02 > v03: # Verificar se são diferentes.
#         print('{} é maior que {} e maior que {}'.format(v01, v02, v03))
#         print()
#     elif v01 > v03 and v03 > v02:
#         print('{} é maior que {} e maior que {}'.format(v01, v03, v02))
#         print()
#     elif v02 > v01 and v01 > v03:
#         print('{} é maior que {} e maior que {}'.format(v02, v01, v03))
#         print()
#     elif v02 > v03 and v03 > v01:
#         print('{} é maior que {} e maior que {}'.format(v02, v03, v01))
#         print()
#     elif v03 > v01 and v01 > v02:
#         print('{} é maior que {} e maior que {}'.format(v03, v01, v02))
#         print()
#     elif v03 > v02 and v02 > v01:
#         print('{} é maior que {} e maior que {}'.format(v03, v02, v01))
#         print()
#     elif v01 == v02 and v02 > v03 or v02 < v03: # Verificar se são parcialmente iguais.
#         print('{} é igual a {} e diferente de {}'.format(v01, v02, v03))
#         print()
#     elif v01 == v03 and v03 > v02 or v03 < v02:
#         print('{} é igual a {} e diferente de {}'.format(v01, v03, v02))
#         print()
#     elif v02 == v01 and v01 > v03 or v01 < v03:
#         print('{} é igual a {} e diferente de {}'.format(v02, v01, v03))
#         print()
#     elif v02 == v03 and v03 > v01 or v03 < v01:
#         print('{} é igual a {} e diferente de {}'.format(v02, v03, v01))
#         print()
#     elif v03 == v01 and v01 > v02 or v01 < v02:
#         print('{} é igual a {} e diferente de {}'.format(v03, v01, v02))
#         print()
#     elif v03 == v02 and v02 > v01 or v02 < v01:
#         print('{} é igual a {} e diferente de {}'.format(v03, v02, v01))
#         print()
#     else: # Mostrar que são iguais.
#         print('Todos os valores são iguais!')
#         print()
# else:
#     print('"{}" não é um valor válido!'.format(v01))
#     print('"{}" não é um valor válido!'.format(v02))
#     print('"{}" não é um valor válido!'.format(v03))
#     print('Digite um valor maior que 0 e sem ponto flutuante!')
#     print()
