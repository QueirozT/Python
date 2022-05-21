from random import randint
from time import sleep

print('===== EXERCÍCIO #088 =====')
print()

print('=' * 30)
print(f'{f"JOGA NA MEGA SENA":^30}') # Formatação de texto com f-string
print('=' * 30)
print()

q = int(input('Quantos jogos você quer que eu sorteie? '))
print()

print(f'-=-=-=  SORTEANDO {q} JOGOS  =-=-=-')

lista = list() # Cria uma lista vazia

for r in range(q): # Criando um contador para o número de jogos.
    lista.append([]) # Adicionando uma Lista vazia na Lista Composta.

    while len(lista[r]) < 6: # Rodando enquanto a Lista[r] dentro da Lista Composta não tiver 6 elementos.
        val = randint(1, 60) # Sorteia um número entre 1 e 60.

        if val not in lista[r]: # Verificando: se o valor sorteado não estiver na Lista[r]
            lista[r].append(val) # Adicione o valor sorteado na Lista[r]

    lista[r].sort() # Re-Ordena a Lista[r]

    print(f'Jogo {r+1}: {lista[r]}') # Imprime a Lista[r]
    sleep(1) # Pausa de 1 segundo.

print('-=-=-=-=-= < BOA SORTE > =-=-=-=-=-')
print()
