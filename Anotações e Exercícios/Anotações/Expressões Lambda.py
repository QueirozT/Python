# EXPRESSÕES LAMBDA: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

# As expressões lambda são funções sem nome, que podem ser passadas como argumentos ou retornadas como valores.
# São muito utilizadas para criar funções de forma rápida.
# Exemplo 01: Criando uma função para somar valores
print('Exemplo 01: Criando uma função para somar valores')
# Criando uma função para somar valores
def soma(a, b):
    return a + b


print('Somando com uma função normal ', soma(1, 2))

# Utilizando uma expressão lambda para somar valores
soma = lambda a, b: a + b
print('Somando com uma expressão lambda ', soma(1, 2))


# Como utilizar expressões lambda?
# ============================== #

# Para utilizar expressões lambda, precisa chamar a palavra-chave lambda,
# em seguida passar os parâmetros da função separados por vírgula ","
# e o que deve acontecer após dois pontos ":"
# Exemplo 02: Utilizando expressão lambda para ordenar uma lista:
print('\nExemplo 02: Utilizando expressão lambda para ordenar uma lista')
lista = [['Pedro', 20], ['Maria', 18], ['Anitha', 24], ['Tiago', 22]]

# Definindo uma função para ordenar as listas pelo indice da lista interna.
def chave(k):
    return k[1]


lista.sort(key=chave)
print('\nOrdenando a lista com uma função comum \n', lista)

# Utilizando uma expressão lambda para ordenar a lista pelo segundo elemento das lista internas.
lista.sort(key=lambda x: x[1]) # x é o parâmetro da func referente a lista, x[1] é o segundo elemento da lista.
print('\nOrdenando a lista com uma expressão lambda \n', lista)
