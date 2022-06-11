# Lista de Dicionários com pessoas para exemplos:
pessoas = [{'Nome': 'Maria', 'Idade': 20}, {'Nome': 'José', 'Idade': 25}, {'Nome': 'Pedro', 'Idade': 30}, {'Nome': 'Marcelo', 'Idade': 22}]
# Lista de Dicionários com produtos para exemplos:
produtos = [{'Produto 01': 'Notebook', 'Preço': 2000}, {'Produto 02': 'Mouse', 'Preço': 80}, {'Produto 03': 'Monitor', 'Preço': 1500}]
# Lista simples para exemplos:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Tupla para exemplos:
tupla = ('Maria', 'José', 'Pedro', 'Marcelo')
# ===================================================================================================================================== #


# Map: É uma função que mapeia um iterável e retorna um Iterador.

# A função map() recebe dois parâmetros e retorna um Iterador:
# Parâmetro 01 - A função que será aplicada a cada elemento da lista (Pode ser uma expressão Lambda).
# Parâmetro 02 - Um objeto iterável (Lista, Tupla, String).
# EX: map(expressão, iterável)

# Como utilizar map()?
# ================== #

# Para utilizar map(), basta chamar a função e informar a função e o objeto iterável como parâmetro.
# Exemplo Map 01: Multiplicado os valores de uma lista com map() e lamba.
print('\nExemplo Map 01: Multiplicando os valores de uma lista com map() e lambda.')
nova_lista = map(lambda x: x * 2, lista)
print('Fazendo um cast e mostrando os valores da nova lista:\n', list(nova_lista))



# Como alterar valores específicos e retornar o objeto modificado com map()?
# ======================================================================== #

# Para alterar valores específicos e retornar o objeto modificado, basta informar a função e o objeto iterável como parâmetro.
# Diferênte do exemplo anterior, a expressão lambda não vai funcionar, pois ela retorna apenas as variáveis informadas.
# Para utilizar uma função definida, basta informar o nome da função que o map vai utilizar o objeto iterável como parâmetro.
# Exemplo Map 02: Alterando os valores de uma lista com map() definindo uma função.
print('\nExemplo Map 02: Alterando os valores de uma lista com map() definindo uma função.')


def aumenta(produto, aumento=10):   # Definindo uma função que recebe uma lista e uma porcentagem (opcional) e altera o valor do produto.
    produto['Preço'] += round(produto['Preço'] * aumento / 100, 2)  # Utilizando a função round() para arredondar o valor com 2 floats.
    return produto


novos_produtos = map(aumenta, produtos)  # Chamando a função aumenta sem executar para que o map execute para cada elemento da lista.
print('Fazendo um cast e mostrando os novos valores dos produtos:\n', list(novos_produtos))



# Como criar novas listas com valores específicos com map()?
# ================================ #

# Para criar novas listas com valores específicos, pode utilizar uma expressão lambda dentro do map retornando o valor específico desejado.
# Exemplo Map 03: Criando uma nova lista com valores específicos com map() e lambda.
print('\nExemplo Map 03: Criando uma nova lista com valores específicos com map() e lambda.')
nomes = map(lambda p: p['Nome'], pessoas)  # Coletando apenas os valores de 'Nome' da lista de dicionários pessoas.
print('Fazendo um cast e mostrando os nomes das pessoas:\n', list(nomes))

# ===================================================================================================================================== #


# Filter: É uma função que filtra um iterável e retorna um Iterador.

# A função filter() recebe dois parâmetros e retorna um Iterador:
# Parâmetro 01 - A função que será aplicada a cada elemento da lista (Pode ser uma expressão Lambda) PS: Precisa retornar Booleano.
# Parâmetro 02 - Um objeto iterável (Lista, Tupla, String).
# EX: filter(expressão, iterável)

# Como utilizar filter()?
# ===================== #

# Para utilizar filter(), basta chamar a função e informar a função que retorne um booleano e o objeto iterável como parâmetro.
# Exemplo Filter 01: Filtrando uma lista com filter() e lambda.
print('\nExemplo Filter 01: Filtrando uma lista de dicionários com filter() e lambda.')
novos_produtos = filter(lambda p: p['Preço'] > 1000, produtos)  # Filtrando apenas os produtos com preço maior que 1000.
print('Fazendo um cast e mostrando os produtos filtrados:\n', list(novos_produtos))

# ===================================================================================================================================== #


# Reduce: É uma função que reduz um iterável e retorna um único valor. ela precisa ser importada de functools.

# A função reduce() recebe três parâmetros e retorna um único valor:
# Parâmetro 01 - Uma expressão lambda contendo dois valores, um acumulador e a variável que irá somar o contador.
# Parâmetro 02 - Um objeto iterável que contenha valores numéricos (Lista, Tupla).
# Parâmetro 03 - Opcional - O valor inicial do acumulador.
# EX: reduce(expressão, iterável, (opcional) indice inicial do iterável)

# como utilizar reduce()?
# ===================== #

# Precisa importar a função reduce de functools para poder utilizar.
# Após importar, basta chamar a função e informar a expressão lambda que retorne um valor numérico e o objeto iterável como parâmetro.
# Exemplo Reduce 01: Somando os valores de uma lista com reduce() e lambda.
print('\nExemplo Reduce 01: Somando os valores de uma lista com reduce() e lambda.')
from functools import reduce  # Importando a função reduce de functools.
soma = reduce(lambda contador, val: contador + val, lista)  # Somando os valores de uma lista.
print('Exibindo a soma dos valores da lista:\n', soma)


# Exemplo Reduce 02: calculando a média das idades de uma lista com reduce() e lambda.
print('\nExemplo Reduce 02: calculando a média das idades de uma lista de dicionários com reduce() e lambda.')
media = reduce(lambda contador, val: contador + val['Idade'], pessoas, 0) / len(pessoas)  # Calculando a média das idades.
print('Exibindo a média das idades:\n', media)
