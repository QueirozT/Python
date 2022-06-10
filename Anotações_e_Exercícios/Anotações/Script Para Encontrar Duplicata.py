"""
Este programa é a solução de um desafio que consiste em iterar valores de listas e identificar o primeiro valor duplicado.
- Caso exista valores duplicados, a primeira ocorrência da duplicação será retornada.
- Caso não exista valores duplicados, será retornado o valor -1.
"""


def duplicata(lista):
    """
    Função que verifica se existe valores duplicados em uma lista e retorna a segunda ocorrência do valor duplicado.
    - lista: Lista que será verificada.
    - return: Retorna o valor duplicado ou -1 caso não exista valores duplicados.
    """
    val = set()
    c = 0
    for v in lista:
        
        val.add(v)
        c += 1
        
        if c != len(val):
            return v
    return -1


lista = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [3, 2, 5, 4, 7, 6, 10, 8, 9, 3],
    [5, 7, 3, 4, 5, 9, 7, 8, 9, 10],
    [2, 5, 8, 1, 7, 9, 2, 4, 8, 10],
    [9, 8, 2, 4, 1, 10, 3, 5, 7, 6],
    [10, 9, 7, 7, 3, 6, 8, 2, 1, 4],
    [7, 6, 4, 3, 2, 1, 5, 10, 9, 8],
    [4, 3, 1, 2, 10, 4, 6, 3, 5, 9],
    [6, 5, 1, 9, 8, 7, 10, 3, 9, 4],
    [8, 7, 9, 8, 6, 5, 3, 1, 2, 10],
]

print('\nLISTAS COM VALORES DUPLICADOS: -1 PARA NÃO DUPLICADOS.')

for v in enumerate(lista):
    print(f'Lista {v} = {duplicata(v[1]):^3}')  # Imprimindo os valores duplicados em cada lista.
print()
