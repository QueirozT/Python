# VARIÁVEIS COMPOSTAS: Tuplas, Listas e Dicionários
# São variáveis que recebem mais de um valor. Podem ser utilizadas para armazenar dados de uma forma mais organizada.


# TUPLAS - As tuplas são variáveis compostas que armazenam mais de um valor dentro de (). Após serem criadas, não podem ser alteradas.

# EXEMPLO 01: Criando uma tupla (O uso de () é opcional nas tuplas)
print('EXEMPLO 01: Criando uma tupla')
tupla = (1, 2, 3, 'Valor 01', 'Valor 02', 'Valor 03')
print(tupla)
print()


# AS TUPLAS TAMBÉM POSSUEM MÉTODOS, COMO:
#=======================================#

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
#=======================================#

# len(lista) - Retorna o tamanho da lista.
# max(lista) - Retorna o maior valor da lista.
# min(lista) - Retorna o menor valor da lista.

# .index(valor) - Retorna o índice da primeira ocorrência de um valor. Pode procurar a partir de um índice específico. EX: .index('t', 2).
# .count(valor) - Retorna a quantidade de ocorrências de um valor dentro da lista.

# .append(valor) - Adiciona um valor no final da lista.
# .insert(indice, valor) - Insere um valor em um índice específico sem substituir valores existentes.

# .sort() - Ordena a lista. Pode inverter a ordem dos elementos com o parâmetro .sort(reverse=True).
# .reverse() - Inverte a ordem dos elementos da lista.

# .copy() - Cria uma cópia da lista. Também pode criar usando "variavel = lista[:]" para que a lista original não seja alterada.

# .remove(valor) - Remove o primeiro "valor" que encontrar.
# .pop(indice) - Remove o valor que está em um índice específico. Se não especificado, o último valor da lista será removido.
# del lista[indice] - Remove um valor específico a lista.
# .clear() - Limpa a lista.

# ======================================================================================================================


# LISTAS COMPOSTAS - As listas compostas são listas que armazenam outras listas, e podem ser acessadas como listas normais.

# As listas compostas também possúem índice, porém, dentro de cada índice existe uma lista com o próprio índice.

# Quando for criar uma lista composta a partir de outras listas, deve-se criar uma copia da lista que será vinculada.
# Ou o Python irá ligar a lista original ao novo índice, e sempre que a lista original for alterada, a lista composta também será alterada.
# EX:
# lista_01 = [1, 2, 3]
# lista_02 = [4, 5, 6]
# lista_03 = [7, 8, 9]
# lista_composta = [lista_01, lista_02, lista_03]
# lista_01[0] = 10
# lista_composta == [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

# O correto quando criar uma lista composta utilizando outras listas é utilizar .copy() ou [:] para criar uma cópia. EX:
# lista_composta = [lista_01[:], lista_02.copy(), lista_03[:]]


# Para acessar os valores de uma lista composta, basta utilizar o índice referente a lista desejada seguido do índice do valor desejado. 
# Exemplo: 
# lista_composta[0][0] = 10
# lista_composta[0][1] = 2
# lista_composta[0][2] = 3


# EXEMPLO 04: Criando uma lista composta
print('EXEMPLO 04: Criando uma lista composta')
lista_composta = [['Pedro', 32], ['Maria', 25], ['João', 28]]
print(lista_composta)
print()

# EXEMPLO 05: Acessando os valores de uma lista composta
print('EXEMPLO 05: Acessando os nomes da lista composta do exercício anterior')
print(lista_composta[0][0])
print(lista_composta[1][0])
print(lista_composta[2][0])
print()
