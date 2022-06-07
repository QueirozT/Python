print('===== EXERCÍCIO #076 =====')
print()

tupla = ('Lápis', 2.00, 'Borracha', 1.50, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)

for i in range(0, len(tupla), 2):
    print(f'{tupla[i]:.<20}', f'R$ {tupla[i+1]:6.2f}')

print('-' * 30)
print()
