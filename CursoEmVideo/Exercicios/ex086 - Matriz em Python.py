print('===== EXERCÍCIO #086 =====')
print()

lista = [[], [], []] # Cria uma lista de 3 listas vazias.

for i in range(3): # Percorre a Lista Composta.
    for j in range(3): # Percorre a Lista dentro da Lista Composta.
        lista[i].append(int(input(f'Digite um valor para: [ {i} ] [ {j} ]: '))) # Adiciona um valor a cada vez que o laço for executado.
        print()

# Percorre as Listas dentro da Lista Composta.
for i in lista:
    for j in i:
        print(f'[ {j} ] ', end='') # Imprime o valor de cada Lista dentro da Lista Composta.
    print('\n')



# FORMA ALTERNATIVA DE APRESENTAR O RESULTADO:

# print(f'[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]')
# print()

# print(f'[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]')
# print()

# print(f'[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]')
# print()


