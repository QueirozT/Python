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

# ======================================================================================================================


# DICIONÁRIOS - Os dicionários são variáveis compostas que armazenam mais de um valor dentro de {} (Chaves).

# Os dicionários servem para armazenar valores assim como as listas, porém, ao invés de índices numéricos, os índices são nomes.

# Para criar um dicionário, basta utilizar {} ou dict().

# EXEMPLO 06: Criando um dicionário
print('EXEMPLO 06: Criando um dicionário')
dicionario = {'nome': 'Pedro', 'idade': 32}
print(dicionario)
print()

# Para acessar os valores de um dicionário, basta utilizar o nome do índice referente ao valor desejado.
# EXEMPLO 07: Acessando os valores de um dicionário
print('EXEMPLO 07: Acessando os valores de um dicionário')
print(dicionario['nome'])
print(dicionario['idade'])
print()

# Para varrer todos os valores de um dicionário, basta utilizar o for.
# EXEMPLO 08: Acessando todos os valores de um dicionário
print('EXEMPLO 08: Acessando todos os valores de um dicionário')
for k, v in dicionario.items():
    print(k, v) # k "Key" e v "Value" | k = nome e v = Pedro
print()

# Também é possível criar dicionários dentro de listas, dicionários dentro de dicionários e vice-versa.
# EXEMPLO 09: Criando um dicionário dentro de outro dicionário
print('EXEMPLO 09: Criando um dicionário dentro de outro dicionário')
dicionario_02 = {'nome': 'Pedro', 'idade': 32, 'filhos': {'nome': 'Maria', 'idade': 25}}
print(dicionario_02)
print()

# EXEMPLO 10: Acessando os valores de um dicionário dentro de outro dicionário
print('EXEMPLO 10: Acessando os valores de um dicionário dentro de outro dicionário')
print(f'Dicionário: {dicionario_02.items()}')
print(f'Filhos: {dicionario_02["filhos"]}')
print(f'Nome do filho: {dicionario_02["filhos"]["nome"]}')
print()


# Criando e lendo um dicionário dentro de uma lista
# EXEMPLO 11: Criando um dicionário dentro de uma lista e lendo o dicionário
print('EXEMPLO 11: Criando um dicionário dentro de uma lista e lendo o dicionário')
estado01 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado02 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado03 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil = [estado01, estado02, estado03]
for i in brasil: # i = cada item da lista
    print(i) # Lendo cada item da lista (dicionário)
    for k, v in i.items(): # k = nome do índice e v = valor do índice
        print(f'{k} = {v}', end=' ') # Lendo cada item do dicionário (chave e valor)
    print()
print()


# OS DICIONÁRIOS TAMBÉM POSSUEM MÉTODOS, COMO:
#============================================#

# dicionario['chave'] = valor - Atualiza o valor de uma chave específica e cria uma nova chave caso não exista.
# .copy() - Cria uma cópia do dicionário. Muito importante para não alterar o dicionário original.
# del dicionario['chave'] - Remove um valor de uma chave específica.

# .values() - Retorna uma lista com os valores do dicionário.
# .keys() - Retorna uma lista com os nomes dos índices do dicionário.
# .items() - Retorna uma lista com tuplas com os índices e valores do dicionário.

# .get(chave) - Retorna o valor de uma chave específica.
# .update(dicionario) - Atualiza o dicionário com os valores de outro dicionário.

# .clear() - Limpa o dicionário.
# .pop(chave) - Remove um valor de uma chave específica.
# .popitem() - Remove um valor aleatório do dicionário.

# sorted(dicionario key=itemgetter(1)) - Retorna uma lista com os valores do dicionário ordenados em forma de tuplas.
# O itemgetter() é uma função que retorna um valor de uma chave específica e precisa ser importado e passada como parâmetro.
# OBS: O itemgetter(1) é o índice referente ao "valor" da chave e o itemgetter(0) é o índice referente ao "nome" da chave.

#=====================================================================================================================

# EXTRA:

# Existem formulas para calcular variáveis compostas como dicionários e listas. uma delas é a formula de média.

# Para calcular a média de um dicionário dentro de uma lista, basta somar todos os valores de cada chave e dividir pelo número de chaves.
# EX: sum(biblioteca[referencia] for identificador in lista) / len(lista)
print('EXEMPLO DE CALCULO DE MÉDIA DE VALORES DE UM DICIONÁRIO DENTRO DE UMA LISTA')
lista = [{'nome': 'Pedro', 'idade': 32}, {'nome': 'Maria', 'idade': 25}]
media = sum(lista['idade'] for lista in lista) / len(lista)
print(lista)
print(f'MÉDIA DAS IDADES: {media:.0f}')
print()
