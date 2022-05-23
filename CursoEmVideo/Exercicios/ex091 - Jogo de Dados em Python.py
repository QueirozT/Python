from random import randint
from time import sleep
from operator import itemgetter

print('===== EXERCÍCIO #091 =====')
print()

jogadores = dict() # Cria um dicionário vazio
rank = list() # Cria uma lista vazia

print('Valores Sorteados:')
for i in range(1, 5):
    jogadores[f'Jogador#0{i}'] = randint(1, 6) # Adiciona um novo valor ao dicionário
    print(f'Jogador#0{i} tirou {jogadores[f"Jogador#0{i}"]} no dado.') # Imprime o valor sorteado
    sleep(1)
print('~~' * 15)


rank = sorted(jogadores.items(), # O sorted() ordena os valores de um dicionário e devolve em formato de lista com tuplas.
key=itemgetter(1), # o key=itemgetter(0 ou 1) serve para selecionar o que vai ser ordenado. 0 = key e 1 = valor.
reverse=True) # O reverse=True serve para ordenar de forma decrescente.

print(f'== RANKING DOS JOGADORES ==')
for i, v in enumerate(rank): # Como o rank é uma lista, o enumerate() serve para mostrar o índice e o valor de cada item da lista.
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos.') # Imprime o índice e o valor de cada item (tuplas) da lista que foi Re-Ordenada.
    sleep(1)
print()
