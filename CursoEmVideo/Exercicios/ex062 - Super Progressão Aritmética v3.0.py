print('===== EXERCÍCIO #62 =====')
print()

print('=-' * 20)
print('{:^40}'.format('PROGRESSÃO ARITMÉTICA'))
print('=-' * 20)
print()

# Primeira parte do programa, desenvolvido no exercício anterior.
valor = int(input('Qual o número? '))
r = int(input('Qual a razão? '))
print()

c = 10

while c != 0:
    print('{}'.format(valor), end=" -> ")
    valor += r
    c -= 1
print('FIM!')
print()

# Segunda parte do programa, responsável por mostrar mais resultados da progressão aritmética.
mais = input('Quer mostrar mais termos? [S/N]: ').upper().strip()
print()

while mais == 'S':
    c = int(input('Quantos termos você quer mostrar a mais? '))
    print()

    while c != 0:
        print('{}'.format(valor), end=" -> ")
        valor += r
        c -= 1
    print('FIM!')
    print()

    mais = input('Quer mostrar mais termos? [S/N]: ').upper().strip()
    print()
