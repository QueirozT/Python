from random import randint

print('===== EXERCÍCIO #45 =====')
print()

print('-=-' * 20)
print('{:^60}'.format('1 - PEDRA | 2 - PAPEL | 3 - TESOURA'))
print('-=-' * 20)
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

if player == 1 and cpu == 1:
    print('EMPATE!')
    print('AMBOS JOGARAM - PEDRA')
    print()
elif player == 1 and cpu == 2:
    print('VOCÊ PERDEU!')
    print('VOCÊ JOGOU - PEDRA')
    print('CPU JOGOU - PAPEL')
    print()
elif player == 1 and cpu == 3:
    print('VOCÊ GANHOU!')
    print('VOCÊ JOGOU - PEDRA')
    print('CPU JOGOU - TESOURA')
    print()
elif player == 2 and cpu == 1:
    print('VOCÊ GANHOU!')
    print('VOCÊ JOGOU - PAPEL')
    print('CPU JOGOU - PEDRA')
    print()
elif player == 2 and cpu == 2:
    print('EMPATE!')
    print('AMBOS JOGARAM - PAPEL')
    print()
elif player == 2 and cpu == 3:
    print('VOCÊ PERDEU!')
    print('VOCÊ JOGOU - PAPEL')
    print('CPU JOGOU - TESOURA')
    print()
elif player == 3 and cpu == 1:
    print('VOCÊ PERDEU!')
    print('VOCÊ JOGOU - TESOURA')
    print('CPU JOGOU - PEDRA')
    print()
elif player == 3 and cpu == 2:
    print('VOCÊ GANHOU!')
    print('VOCÊ JOGOU - TESOURA')
    print('CPU JOGOU - PAPEL')
    print()
elif player == 3 and cpu == 3:
    print('EMPATE!')
    print('AMBOS JOGARAM - TESOURA')
    print()
else:
    print('Opção inválida!')
    print()
