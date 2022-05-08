from random import randint, choice
from time import sleep

print('===== EXERCÍCIO 28 =====')
print()

number = randint(0, 5) # Variável que recebe um número aleatório entre 0 e 5.

# Primeira interação do programa.
print('-=-' * 20)
print('{:^20}'.format('Estou pensando em um número entre 0 e 5. tente adivinhar...'))
print('-=-' * 20)
print()

# Coleta do número do usuário.
value = input('Em que número eu pensei? ')
print()

# mensagem de espera.
print('Só um segundo...')
print()
sleep(3)

# Mensagens alternativas para interação com o usuário.
memoria = choice(['a', 'b', 'c', 'd'])

if memoria == 'a' or memoria == 'd':
    print('O que eu est...')
    print()
    sleep(4)

    print('AHHHH LEMBREI!')
    print()
    sleep(2)

    print('Desculpe por isso, memória cheia sabe...')
    print()
    sleep(2)
elif memoria == 'b' or memoria == 'c':
    print('Desculpe pela demora...')
    print()
    sleep(2)

    print('Estava limpando o cachê :)')
    print()
    sleep(2)

# Resultado e ultima interação do programa.
if value.isnumeric():
    value = int(value)

    if value == number:
        print('Parabéns! eu estava mesmo pensando em "{}"'.format(number))
    elif value > 5:
        print('Você não entendeu as regras. "{}" não está entre 0 e 5.'.format(value))
    else:
        print('Você errou! eu estava pensando em "{}"'.format(number))
    print()
else:
    print('Você é burro? "{}" não é um número.'.format(value))
    print()
