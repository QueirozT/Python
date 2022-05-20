# VARIÁVEIS COMPOSTAS: Tuplas, Listas e Dicionários
# São variáveis que recebem mais de um valor. Podem ser utilizadas para armazenar dados de uma forma mais organizada.


# TUPLAS - As tuplas são variáveis compostas que armazenam mais de um valor dentro de (). Após serem criadas, não podem ser alteradas.

# EXEMPLO 01: Criando uma tupla (O uso de () é opcional nas tuplas)
print('EXEMPLO 01: Criando uma tupla')
tupla = (1, 2, 3, 'Valor 01', 'Valor 02', 'Valor 03')
print(tupla)
print()


# AS TUPLAS TAMBÉM POSSUEM MÉTODOS, COMO:
# .count(valor) - Retorna a quantidade de ocorrências de um valor dentro da tupla.
# .index(valor) - Retorna o índice da primeira ocorrência de um valor. Pode procurar a partir de um índice específico. EX: .index('t', 2).
# del(tupla) - Remove a tupla.

# Apesar de não permitir alterações, as tuplas podem ser concatenadas com outras tuplas ou convertidas em listas.

# ======================================================================================================================


# LISTAS - As listas são variáveis compostas que armazenam mais de um valor dentro de [] (Colchetes). Estas podem ser alteradas.

# EXEMPLO 02: Criando uma lista
print('EXEMPLO 02: Criando uma lista')
lista = [1, 2, 3, 'Valor 01', 'Valor 02', 'Valor 03']
print(lista)
print()


# EXEMPLO 03: Criando uma lista através do metodo list()
print('EXEMPLO 03: Criando uma lista através do metodo list()')
lista = list(range(1, 11))
print(lista)
print()


# AS LISTAS TAMBÉM POSSUEM MÉTODOS, COMO:
# .append(valor) - Adiciona um valor no final da lista.
# .insert(indice, valor) - Insere um valor em um índice específico sem substituir valores existentes.

# len(lista) - Retorna o tamanho da lista.
# .index(valor) - Retorna o índice da primeira ocorrência de um valor. Pode procurar a partir de um índice específico. EX: .index('t', 2).
# .count(valor) - Retorna a quantidade de ocorrências de um valor dentro da lista.

# .sort() - Ordena a lista. Pode inverter a ordem dos elementos com o parâmetro .sort(reverse=True).
# .reverse() - Inverte a ordem dos elementos da lista.

# .copy() - Cria uma cópia da lista.
# .remove(valor) - Remove o primeiro "valor" que encontrar.
# .pop(indice) - Remove o valor que está em um índice específico. Se não especificado, o último valor da lista será removido.
# del lista[indice] - Remove um valor específico a lista.
# .clear() - Limpa a lista.

# ======================================================================================================================
