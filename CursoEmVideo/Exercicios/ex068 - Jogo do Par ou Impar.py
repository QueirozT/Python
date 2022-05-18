from random import randint

print('===== EXERCÍCIO #68 =====')
print()

print('=-=' * 10)
print('{:^30}'.format('VAMOS JOGAR PAR OU IMPAR!'))
print('=-=' * 10)
print()

# Contador de jogadas
c = 0

while True:
# Gerar um número aleatório entre 0 e 10
    cpu = randint(0, 10) 

# Receber o valor do usuário
    valor = int(input('Qual o valor? '))

# Loop para verificar se o valor é par ou ímpar
    while True:
        opcao = input('Par ou Impar? [P/I] ').upper().strip()[0]
        if opcao in 'PI':
            break
    print()

# Verificar se deu par ou ímpar
    if opcao == 'P':
        if (valor + cpu) % 2 == 0:
            r = 'PAR'
        else:
            r = 'IMPAR'
    elif opcao == 'I':
        if (valor + cpu) % 2 != 0:
            r = 'IMPAR'
        else:
            r = 'PAR'

# Verificar se o usuário venceu ou perdeu
    print('=-=' * 30)
    if opcao == r[0]:
        print('{:^90}'.format(f'Você venceu! Você jogou "{valor}" e o computador Jogou "{cpu}" O resultado é "{r}"!'))
        print('{:^90}'.format('Vamos jogar novamente...'))
        print('=-=' * 30)
        print()
        c += 1
    else:
        print('{:^90}'.format(f'Game Over! Você jogou "{valor}" e o computador Jogou "{cpu}" O resultado é "{r}"!'))
        print('=-=' * 30)
        print()
        break

# Mostrar o placar final
if c == 1:
    print(f'Você venceu {c} vez.')
elif c == 0:
    print(f'Você perdeu de primeira!')
else:
    print(f'Você venceu {c} vezes.')
print()
