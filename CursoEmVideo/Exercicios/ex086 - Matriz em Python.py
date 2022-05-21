print('===== EXERCÍCIO #086 =====')
print()

lista = [[], [], []] # Cria uma lista composta com 3 listas vazias.

for l in range(3): # Percorre a Lista Composta.
    for c in range(3): # Percorre a Lista dentro da Lista Composta.
        lista[l].append(int(input(f'Digite um valor para: [ {l} ] [ {c} ]: '))) # Adiciona um valor a cada vez que o laço for executado.
print()

# Percorre as Listas dentro da Lista Composta.
for l in lista:
    for c in l:
        print(f'[{c:^5}]', end='') # Imprime o valor de cada Lista dentro da Lista Composta.
    print('\n')



# FORMA ALTERNATIVA DE APRESENTAR O RESULTADO:

# print(f'[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]')
# print()

# print(f'[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]')
# print()

# print(f'[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]')
# print()



# PROGRAMA ALTERNATIVO:

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Cria uma matriz 3x3 vazia.

# for l in range(3): # percorre a linha da matriz.
#     for c in range(3): # percorre as colunas da linha[l] da matriz.
#         matriz[l][c] = int(input(f'Digite um valor para: [ {l} ] [ {c} ]: ')) # Adiciona o valor digitado a linha[l] na coluna[c].
# print()

# for l in range(3):
#     for c in range(3):
#         print(f'[{matriz[l][c]:^5}]', end='') # Percorre as colunas[c] de cada linha[l] da matriz e imprime o valor formatado. 
#     print('\n')
