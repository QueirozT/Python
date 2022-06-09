# SETS: Os sets são conjuntos de elementos sem ordem e não podem conter elementos repetidos.

# Os sets assim como os dicionários são definidos com chaves {}, porém só podem conter valores únicos.
# EXEMPLO: set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Eles também podem ser definidos como conjuntos vazios, EXEMPLO: set = set()

# Os sets não podem conter valores identicos, então normalmente são utilizados para eliminar valores duplicados de listas.
# EXEMPLO 01: Removendo valores duplicados de uma lista:
print('Removendo valores duplicados de uma lista:')
lista = [1, 2, 3, 1, 2, 3, 1, 3, 2, 3]
print(f'\nLista Original: {lista}')

lista = list(set(lista))  # Fazendo um cast de "set" para "list" para remover os valores duplicados de uma lista.
print(f'\nLista sem os valores duplicados: {lista}')


# OS SETS TAMBÉM POSSUEM MÉTODOS:
# ============================= #

# Os métodos disponíveis para os sets são:

# - add(elemento): Adiciona um elemento ao set.
# - update(iterável): Adiciona vários elementos ao set (é usado para adicionár as letras de frases/palavras).
# - discard(elemento): Remove o elemento do set se ele existir.
# - clear(): Limpa o set.

# - union(set): Retorna o conjunto de todos os elementos dos dois sets.
# - intersection(set): Retorna apenas os valores entre o set e o set passado como parâmetro.
# - difference(set): Retorna os valores que estão apenas no set e não no set passado como parâmetro (Esquerda).
# - simetric_difference(set): Retorna os valores que estão apenas no set passado como parâmetro (Direita).



# Como utilizar simbolos ao invés de métodos?
# ========================================= #

# Para utilizar simbolos ao invés de métodos, basta utilizar o símbolo do set como se fosse uma variável.
# EXEMPLO:
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = s1 | s2  # Retorna o conjunto de todos os elementos dos dois sets sem repetir valores.

print(f'\nS1: {s1}')
print(f'S2: {s2}')
print(f'S3: {s3}')


# Simbolos:
# ======= #

# - |: Union (Retorna todos os elementos dos dois sets).
# - &: Intersection (Retorna apenas os elementos que estão em ambos os sets).
# - -: Difference (Retorna os elementos que estão apenas no set e não no set passado como parâmetro).
# - ^: Simetric difference (Retorna os elementos que estão apenas no set passado como parâmetro e não no set).
