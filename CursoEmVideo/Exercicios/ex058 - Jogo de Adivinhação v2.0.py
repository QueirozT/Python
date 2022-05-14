from random import randint

print('===== EXERCÍCIO #58 =====')
print()

print('-=' * 20)
print('{:^40}'.format('JOGO DE ADIVINHAÇÃO!'))
print('-=' * 20)
print()

cpu = randint(0, 10)

print('Estou pensando em um número entre 0 e 10. Tente adivinhar...')
print()

tentativas = 0

jogador = ''

while jogador != cpu:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador != cpu:
        print('Você errou! Tente novamente!')
        print()
print('Parabéns! você acertou, mas precisou de {} tentativas!'.format(tentativas))
print()
