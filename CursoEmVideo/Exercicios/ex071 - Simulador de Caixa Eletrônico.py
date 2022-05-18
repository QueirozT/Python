print('===== EXERCÍCIO #71 =====')
print()

print('==' * 20)
print('{:^40}'.format('BANCO GRATIS'))
print('==' * 20)
print()

valor = int(input('Quanto deseja sacar? R$'))
print()

S50 = S20 = S10 = S1 = 0

while True:
    if valor >= 50:
        valor -= 50
        S50 += 1
    elif valor >= 20:
        valor -= 20
        S20 += 1
    elif valor >= 10:
        valor -= 10
        S10 += 1
    elif valor >= 1:
        valor -= 1
        S1 += 1
    else:
        break

print('{:~^40}'.format(' SACANDO '))
if S50 > 0:
    print('{:^40}'.format(f'{S50} cédulas de R$50.00'))
if S20 > 0:
    print('{:^40}'.format(f'{S20} cédulas de R$20.00'))
if S10 > 0:
    print('{:^40}'.format(f'{S10} cédulas de R$10.00'))
if S1 > 0:
    print('{:^40}'.format(f'{S1} cédulas de R$1.00'))
print('~~' * 20)
print()


# PROGRAMA ALTERNATIVO:

# print('=' * 30)
# print('{:^30}'.format('BANCO CEV'))
# print('=' * 30)
# print()

# valor = int(input('Quanto deseja sacar? R$'))
# print()

# total = valor # Guarda o valor sacado
# ced = 50 # Guarda o valor da cédula atual (mais alta)
# totced = 0 # Guarda quantas vezes a cédula mais alta é usada

# while True:
#     if total >= ced: # Verifica se o valor sacado pode ser subtraído da cédula atual
#         total -= ced
#         totced += 1
#     else: # Se não, a cédula atual é descartada e a próxima é usada

#         if totced > 0: # Verifica se a cédula atual foi usada
#             print(f'Total de {totced} cédulas de R${ced}') # Imprime quantas vezes a cédula atual foi usada.

#         # Verifica qual a próxima cédula a ser usada para o valor restante
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1

#         # Limpa o contador de cédulas para a próxima cédula
#         totced = 0
        
#         # Verifica se o valor restante é zero para sair do laço
#         if total == 0:
#             break

# print('=' * 30)
# print('{:^30}'.format('Volte sempre ao BANCO CEV!'))
# print()
