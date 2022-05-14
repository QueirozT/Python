print('===== EXERCÍCIO #55 =====')
print()

peso = [] # cria uma lista vazia

for i in range(0, 5):
    peso += [int(input("Digite o peso: "))]
print()

print('O maior valor é {}'.format(max(peso))) # max() retorna o maior valor de um iterável.
print('O menor valor é {}'.format(min(peso))) # min() retorna o menor valor de um iterável.
print()


# VERSÃO ALTERNATIVA DO PROGRAMA:

# maior = 0
# menor = 0

# for i in range(5):
#     peso = int(input("Qual o peso da {}ª pessoa? ".format(i+1)))
#     if i == 0:
#         maior = peso
#         menor = peso
#     if peso > maior:
#         maior = peso
#     if peso < menor:
#         menor = peso
# print()

# print('O maior valor registrador foi {}'.format(maior))
# print('E o menor valor registrador foi {}'.format(menor))
# print()
