print('===== EXERCÍCIO #55 =====')
print()

peso = [] # cria uma lista vazia

for i in range(0, 5):
    peso += [int(input("Digite o peso: "))]
print()

print('O maior valor é {}'.format(max(peso))) # max() retorna o maior valor de um iterável.
print('O menor valor é {}'.format(min(peso))) # min() retorna o menor valor de um iterável.
print()
