from random import randint

print('===== EXERCÍCIO 28 =====')
print()

number = randint(0, 5) # Variável que recebe um número aleatório entre 0 e 5

print('Este é um jogo de adivinhação.')
value = input('Estou pensando em um número entre 0 e 5, qual você acha que é? ')
print()

if value.isnumeric():
    value = int(value)

    if value == number:
        print('Parabéns, você é muito bom! eu estava mesmo pensando em "{}"'.format(number))
    elif value > 5:
        print('Você não entendeu as regras, "{}" não está entre 0 e 5.'.format(value))
    else:
        print('Sinto muito, você errou! eu estava pensando em "{}"'.format(number))
    print()
else:
    print('"{}" não é um número, não quer brincar comigo? T-T'.format(value))
    print()
