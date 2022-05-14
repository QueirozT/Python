from datetime import datetime
print('===== EXERCÍCIO #54 =====')
print()

maior = 0
menor = 0

atual = datetime.now().year

for i in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))

    idade = atual - ano

    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
print()

if maior > 0 and menor > 0:
    print('Dos 7 que você digitou, {} são maiores de idade e {} são menores de idade.'.format(maior, menor))
elif maior > 0 and menor == 0:
    print('Dos 7 que você digitou, {} são maiores de idade.'.format(maior))
elif maior == 0 and menor > 0:
    print('Dos 7 que você digitou, {} são menores de idade.'.format(menor))
print()
