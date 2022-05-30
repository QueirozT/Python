from ex107 import metade, dobro, aumentando

print('===== EXERCÍCIO #107 =====')
print()

v = float(input('Digite o preço: R$'))

print(f'A metade de {v} é {metade(v)}.')
print(f'O dobro de {v} é {dobro(v)}.')
print(f'Aumentando 10%, temos {aumentando(v, 10)}.')
