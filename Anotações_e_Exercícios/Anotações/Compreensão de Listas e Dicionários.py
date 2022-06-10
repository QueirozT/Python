# Compreensão de Listas: Ou list comprehension é uma forma de iterar sobre listas de forma mais eficiente.

# Quando você tem uma lista ou tupla e quer fazer algo com cada elemento da lista, você não precisa usar um for.
# Você pode usar list comprehensions para iterar.

# Como utilizar list comprehensions?
# ================================ #

# Para utilizar list comprehensions, você precisa escrever entre colchetes o código com o que deseja fazer.
# O código que você escrever entre colchetes será executado para cada elemento da lista e o resultado será uma nova lista.
# Exemplo 01:
print('Exemplo 01: Compressão de listas.')
lista = list(range(30))  # Cria uma lista com 30 elementos
print('Lista Normal \n', lista)

modificada = [v for v in lista if v % 2 == 0 if v % 3 == 0]
print('\nLista Modificada: Apenas divisiveis por 2 e 3: \n', modificada)



# Como Iterar com List Comprehensions?
# ================================== #

# Para iterar valores com List Comprehensions basta declarar entre colchetes:
# 1 - Uma variável para desenpacotar cada item da lista: v
# 2 - Um for com a variável e o nome da lista que deseja iterar: for v in lista
# Exemplo 02:
print('\nExemplo 02: Iterando com List Comprehensions.')
lista = list(range(1, 11))
print('Exibindo todos os valores da lista:\n', [v for v in lista])



# Alterando valores com List Comprehensions:
# ======================================== #

# Para alterar valores, é só seguir os passos utilizados para iterar, declarando na variável o que fazer.
# Exemplo 03:
print('\nExemplo 03: Alterando valores com List Comprehensions')
lista = ['José', 'Maria', 'Pedro', 'Roberta']
print('Alterando as letras "O" para "0" e "A" para "@"\n', [v.replace('o', '0').replace('a', '@') for v in lista])



# Usando Condicionais simples com List Comprehensions:
# ================================================== #

# Para utilizar Condicionais simples em uma List Comprehension, basta informar a ou as condições após declarar o for.
# Exemplo 04:
print('\nExemplo 04: Condicionais simples com List Comprehensions')
lista = list(range(1, 31))
print('Exibindo apenas os valores de 1 a 30 que são divisíveis por 3:\n', [v for v in lista if v % 3 == 0])



# Utilizando multiplos laços "for" com List Comprehensions:
# ====================================================== #

# Para utilizar multiplos laços for, basta inserir um for após o anterior. 
# Exemplo 05:
print('\nExemplo 05: Gerando tuplas com multiplos for')
lista = list(range(4))
print('Exibindo Tuplas com 2 indices cada para cada item da lista:\n', [(v1, v2) for v1 in lista for v2 in range(2)])



# Utilizando Condicionais Compostas com List Comprehensions:
# ======================================================== #

# Utilizar condicional composta é diferente de utilizar condicionais simples.
# Quando utilizamos condicionais compostas, precisamos declarar antes do for após a variável.
# Exemplo 06:
print('\nExemplo 06: Utilizando Condicionais Compostas IF ELSE')
lista = list(range(10))
print('Exibindo valores pares divisíveis por 3 e -1 para os demais.\n', [v if v % 2 ==0 and v % 3 == 0 else -1 for v in lista])



# Separando valores e formatando com List Comprehensions:
# ======================================== #

# Quando não podemos usar o .splite() por não haver um caractere para separar, e a string possui um padrão.
# Podemos utilizar o List Comprehensions. Uma das formas de utilizar é fazendo um fatiamento com o range() do for.
# Para isso, chamo a variável que quero fatiar e dentro dos colchetes uso o range do for para definir o espaço que quero fatiar.
# Exemplo 07:
print('\nExemplo 07: Iterando e Separando valores')
string = '012345678901234567890123456789012345678901234567890123456789'
print('String Sem Alteração:\n', string)

lista = [string[v:v+10] for v in range(0, len(string), 10)]
print('\nIterando e Separando valores:\n', lista)

novaString = '.'.join(lista)
print('\nExibindo a nova string, agora separada por .\n', novaString)
print()

# ====================================================================================================================== #


# Dictionary Comprehensions:
# ======================== #

# A compreensão de dicionários assim como a compreensão de listas é uma forma de iterar sobre dicionários.
# Quando você tem um dicionário e quer fazer algo com cada chave ou elemento do dicionário, você não precisa usar um for.
# Você pode usar dictionary comprehensions para iterar.

# Para iterar sobre um dicionário, basta utilizar chaves {} ao invés de colchetes [], e separar as chaves e valores com dois pontos.
# Exemplo 08:
print('\nExemplo 08: Iterando com Compreensão de Dicionários')
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print('Multiplicando os valores de um Dicionário:\n', {k: v * 2 for k, v in dicionario.items()})



# Alterando valores de um dicionário com Compreensão de Dicionários:
# ================================================================ #

# Para alterar valores de um dicionário, basta utilizar o mesmo padrão de compreensão de listas, informando a chave e o valor.
# Lembrando que a chave e o valor precisam estar separados por : ou o resultado não será um "dicionário", mas sim um "set".
# Exemplo 09:
print('\nExemplo 09: Alterando valores de um Dicionário')
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print('Alterando os valores de um Dicionário:\n', {k.upper(): v + 2 for k, v in dicionario.items()})



# Convertendo uma lista em um dicionário com Compreensão de Dicionários:
# ==================================================================== #

# Para fazer um "cast" dict() e converter uma Lista em um dicionário, a lista precisa conter pares chave/valor.
# Converter utilizando a compreensão de dicionários te permite fazer alterações que o cast dict() não permite.
# Exemplo 10:
print('\nExemplo 10: Convertendo uma Lista em um Dicionário')
lista = ['a', 'b', 'c', 'd', 'e']
print('Convertendo uma Lista em um Dicionário:\n', {k: v for k, v in enumerate(lista)})



# Convertendo tuplas em dicionários com Compreensão de Dicionários:
# =============================================================== #

# Para fazer um "cast" dict() e converter uma Tupla em um dicionário, assim como em listas a tupla precisa conter pares chave/valor.
# Converter utilizando a compreensão de dicionários te permite fazer alterações que o cast dict() não permite.
# Também pode criar chaves e valores se a tupla tiver um tamanho resultante em par.
# Exemplo 11:
print('\nExemplo 11: Convertendo uma Tupla em um Dicionário')
tupla = ('a', 'Maria', 'b', 'Pedro', 'c', 'José')
print('Convertendo uma Tupla em um Dicionário:\n', {tupla[v]: tupla[v + 1] for v in range(0, len(tupla), 2)})



# Criando indices e convertendo uma lista em dicionário com Compreensão de Dicionários:
# =================================================================================== #

# Para criar indices, basta utilizar uma f-string com o nome da chave e o valor que quero que seja o indice.
# Exemplo 12:
print('\nExemplo 12: Convertendo uma lista e Criando indices para um Dicionário')
lista = ['Maria', 'Pedro', 'anitha', 'Felipe', 'Roberta']
print('Convertendo uma lista em um Dicionário:\n', {f'Pessoa {k}': v for k, v in enumerate(lista)})
print()
