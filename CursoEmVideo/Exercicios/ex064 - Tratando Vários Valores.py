print('===== EXERCÍCIO #64 =====')
print()

print('Iniciando...')
print()

print('Para parar a leitura, insira 999 no campo de valor.')
print()

soma = cont = 0
valor = 0

while valor != 999:
    valor = int(input('Qual o valor? '))
    if valor != 999:
        soma += valor
        cont += 1
    print()
print('Finalizando...')
print()

print('A soma de todos os {} valores digitados é {}.'.format(cont, soma))
print()



# PROGRAMA ALTERNATIVO (Sem utilizar o if):

# print('Para finalizar a leitura, insira 999 no campo de valor.')
# print()

# soma = cont = 0

# valor = int(input('Qual o valor? '))
# print()

# while valor != 999:
#     soma += valor
#     cont += 1
#     valor = int(input('Qual o valor? ')) # Adicionando o valor ao final do loop, o flag "999" não é considerado no somatório.
#     print()

# print('Você digitou {} números e a soma de todos eles é {}.'.format(cont, soma))
# print()
