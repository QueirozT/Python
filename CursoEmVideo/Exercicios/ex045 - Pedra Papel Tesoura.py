from random import randint
from time import sleep

print('===== EXERCÍCIO #45 =====')
print()

print('{:^40}'.format('JOKENPÔ!!!'))
print('-=' * 20)
print('{:^40}'.format('1 - PEDRA | 2 - PAPEL | 3 - TESOURA'))
print('-=' * 20)
print()

cpu = randint(1, 3)

player = input('Escolha sua jogada: ')
print()

if player.isnumeric():
    player = int(player)
else:
    player = player.upper()
    if 'PEDRA' in player:
        player = 1
    elif 'PAPEL' in player:
        player = 2
    elif 'TESOURA' in player:
        player = 3

print('JO')
sleep(2)

print('KEN')
sleep(2)

print('PO!!!')

print('-=' * 20)
if player == 1 and cpu == 1:
    print('{:^40}'.format('EMPATE!'))
    print('{:^40}'.format('AMBOS JOGARAM - PEDRA'))
elif player == 1 and cpu == 2:
    print('{:^40}'.format('VOCÊ PERDEU!'))
    print('{:^40}'.format('VOCÊ JOGOU - PEDRA'))
    print('{:^40}'.format('CPU JOGOU - PAPEL'))
elif player == 1 and cpu == 3:
    print('{:^40}'.format('VOCÊ GANHOU!'))
    print('{:^40}'.format('VOCÊ JOGOU - PEDRA'))
    print('{:^40}'.format('CPU JOGOU - TESOURA'))
elif player == 2 and cpu == 1:
    print('{:^40}'.format('VOCÊ GANHOU!'))
    print('{:^40}'.format('VOCÊ JOGOU - PAPEL'))
    print('{:^40}'.format('CPU JOGOU - PEDRA'))
elif player == 2 and cpu == 2:
    print('{:^40}'.format('EMPATE!'))
    print('{:^40}'.format('AMBOS JOGARAM - PAPEL'))
elif player == 2 and cpu == 3:
    print('{:^40}'.format('VOCÊ PERDEU!'))
    print('{:^40}'.format('VOCÊ JOGOU - PAPEL'))
    print('{:^40}'.format('CPU JOGOU - TESOURA'))
elif player == 3 and cpu == 1:
    print('{:^40}'.format('VOCÊ PERDEU!'))
    print('{:^40}'.format('VOCÊ JOGOU - TESOURA'))
    print('{:^40}'.format('CPU JOGOU - PEDRA'))
elif player == 3 and cpu == 2:
    print('{:^40}'.format('VOCÊ GANHOU!'))
    print('{:^40}'.format('VOCÊ JOGOU - TESOURA'))
    print('CPU JOGOU - PAPEL')
elif player == 3 and cpu == 3:
    print('{:^40}'.format('EMPATE!'))
    print('{:^40}'.format('AMBOS JOGARAM - TESOURA'))
else:
    print('{:^40}'.format('Opção inválida!'))
print('-=' * 20)
print()


# VERSÃO ALTERNATIVA DO PROGRAMA.

# from random import randint
# from time import sleep

# itens = ['pedra', 'papel', 'tesoura']

# computador = randint(0, 2)

# print('''SUAS OPÇÕES:
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA''')

# jogador = int(input('Qual é a Sua jogada? '))

# print('JO')
# sleep(1)
# print('KEN')
# sleep(1)
# print('PO!!!')

# print('-=' * 11)
# print('COMPUTADOR JOGOU {}'.format(itens[computador]))
# print('JOGADOR JOGOU {}'.format(itens[jogador]))
# print('-=' * 11)

# if computador == 0: # Computador jogou PEDRA
#     if jogador == 0:
#         print('EMPATE!')
#     elif jogador == 1:
#         print('JOGADOR VENCE!')
#     elif jogador == 2:
#         print('COMPUTADOR VENCE!')
#     else:
#         print('JOGADA INVÁLIDA!')

# elif computador == 1: # Computador jogou PAPEL
#     if jogador == 0:
#         print('COMPUTADOR VENCE!')
#     elif jogador == 1:
#         print('EMPATE!')
#     elif jogador == 2:
#         print('JOGADOR VENCE!')
#     else:
#         print('JOGADA INVÁLIDA!')

# elif computador == 2: # Computador jogou TESOURA
#     if jogador == 0:
#         print('JOGADOR VENCE!')
#     elif jogador == 1:
#         print('COMPUTADOR VENCE!')
#     elif jogador == 2:
#         print('EMPATE!')
#     else:
#         print('JOGADA INVÁLIDA!')
