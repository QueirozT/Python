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
