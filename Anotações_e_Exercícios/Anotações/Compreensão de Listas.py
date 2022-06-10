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
