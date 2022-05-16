from ast import Break
from random import randint

print('===== EXERCÍCIO #58 =====')
print()

print('-=' * 20)
print('{:^40}'.format('JOGO DE ADIVINHAÇÃO!'))
print('-=' * 20)
print()

cpu = randint(0, 10)

print('Estou pensando em um número entre 0 e 10...')
print()

tentativas = 0

jogador = int(input('Qual é o seu palpite? '))

while jogador != cpu:
    if jogador > 10 or jogador < 0:
        print('"{}" não vale! tente de novo.'.format(jogador))
        print()
    elif jogador < cpu:
        print('Você errou! é um pouco mais...')
        print()
    elif jogador > cpu:
        print('Você errou! é um pouco menos...')
        print()
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1

if tentativas == 0:
    print('Parabéns! Você acertou de primeira!')
    print()
else:
    print('Parabéns! Você acertou, mas precisou de {} tentativas.'.format(tentativas))
    print()
