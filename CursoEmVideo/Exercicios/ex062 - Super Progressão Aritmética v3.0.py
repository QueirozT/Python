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

c = quantidade = 10

while c != 0:
    print('{}'.format(valor), end=" -> ")
    valor += r
    c -= 1
print('FIM!')
print()

# Segunda parte do programa, responsável por mostrar mais resultados da progressão aritmética.
mais = input('Quer mostrar mais termos? [S/N]: ').upper().strip()
print()

while mais not in 'SN': # Validação para garantir que o usuário digite apenas S ou N.
    print('Opção inválida!')
    mais = input('Quer mostrar mais termos? [S/N]: ').upper().strip()
    print()

while mais == 'S':
    c = int(input('Quantos termos você quer mostrar a mais? '))
    print()

    quantidade += c # Número de termos que o usuário quer mostrar.

    while c != 0:
        print('{}'.format(valor), end=" -> ")
        valor += r
        c -= 1
    print('FIM!')
    print()

    mais = input('Quer mostrar mais termos? [S/N]: ').upper().strip()
    print()

    while mais not in 'SN':
        print('Opção inválida!')
        mais = input('Quer mostrar mais termos? [S/N]: ').upper().strip()
        print()

if mais == 'N':
    print('=-=' * 20)
    print('{:^60}'.format('A progressão foi finalizada após exibir {} termos.'.format(quantidade)))
    print('=-=' * 20)
print()


# PROGRAMA ALTERNATIVO (SIMPLIFICADO):

# print('-=' * 10)
# print('{:^20}'.format('GERADOR DE PA'))
# print('-=' * 10)

# razao = int(input('Informe a razão: '))
# primeiro = int(input('Informe o primeiro termo: '))
# print()

# termo = primeiro
# cont = 1
# total = 0
# mais = 10

# while mais != 0:
#     total += mais
#     while cont <= total:
#         print('{} -> '.format(termo), end='')
#         termo += razao
#         cont += 1
#     print('PAUSA!')
#     print()
#     mais = int(input('Quantos termos você quer mostrar a mais? '))
#     print()

# print('Progressão finalizada com {} termos mostrados.'.format(total))
# print()
