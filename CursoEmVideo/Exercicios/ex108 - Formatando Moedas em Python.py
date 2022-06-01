import ex108Moeda as moeda

print('===== EXERCÍCIO #108 =====')
print()

v = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.valor(v)} é {moeda.valor(moeda.metade(v))}.')
print(f'O dobro de {moeda.valor(v)} é {moeda.valor(moeda.dobro(v))}')
print(f'Aumentando 10%, temos {moeda.valor(moeda.aumentar(v, 10))}')
print()
