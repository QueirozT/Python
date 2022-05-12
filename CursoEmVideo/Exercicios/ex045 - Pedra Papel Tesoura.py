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
