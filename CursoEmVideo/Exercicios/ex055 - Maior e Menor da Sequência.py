print('===== EXERCÍCIO #55 =====')
print()

peso = []

for i in range(0, 5):
    peso += [int(input("Digite o peso: "))]
print()

print('O maior valor é {}'.format(max(peso)))
print('O menor valor é {}'.format(min(peso)))
print()
