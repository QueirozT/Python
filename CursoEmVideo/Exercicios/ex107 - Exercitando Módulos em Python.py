import ex107Moeda as moeda # Importando o módulo e dando um apelido para facilitar o chamado.

print('===== EXERCÍCIO #107 =====')
print()

v = float(input('Digite o preço: R$'))

print(f'A metade de {v} é {moeda.metade(v)}.')
print(f'O dobro de {v} é {moeda.dobro(v)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(v, 10)}.')
print()
