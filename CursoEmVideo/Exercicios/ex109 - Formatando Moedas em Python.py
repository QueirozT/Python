import ex109Moeda as moeda

print('===== EXERCÍCIO #109 =====')
print()

v = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(v)} é {moeda.metade(v, True)}.')
print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro(v, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(v, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(v, 13, True)}')
print()
