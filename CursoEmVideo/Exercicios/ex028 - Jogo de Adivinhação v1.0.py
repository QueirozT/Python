from random import randint

print('===== EXERCÍCIO 28 =====')
print()

number = randint(0, 5) # Variável que recebe um número aleatório entre 0 e 5

print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
print()

value = input('Em que número eu pensei? ')
print()

if value.isnumeric():
    value = int(value)

    if value == number:
        print('Você é muito bom! eu estava mesmo pensando em "{}"'.format(number))
    elif value > 5:
        print('Você não entendeu as regras. "{}" não está entre 0 e 5.'.format(value))
    else:
        print('Você errou! eu estava pensando em "{}"'.format(number))
    print()
else:
    print('Você é burro? "{}" não é um número...'.format(value))
    print()
