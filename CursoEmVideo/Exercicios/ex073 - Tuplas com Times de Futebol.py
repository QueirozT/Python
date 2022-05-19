print('===== EXERCÍCIO #073 =====')
print()

tupla = ('Corinthians', 'Atlético-MG', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba', 'Avaí', 'América-MG', 'Palmeiras', 'Bragantino', 'Internacional', 'Fluminense', 'Goiás', 'Cuiabá', 'Athletico-PR', 'Flamengo', 'Juventude', 'Ceará SC', 'Atlético-GO', 'Fortaleza')

print('Os 5 primeiros colocados são: ', end='')
for i in range(5):
    print(tupla[i], end=', ')
print()
print()

print('Os últimos 4 colocados são: ', end='')
for i in range(len(tupla) -4, len(tupla)):
    print(tupla[i], end=', ')
print()
print()

print('Em ordem alfabética: ', end='')
for i in sorted(tupla):
    print(i, end=', ')
print()
print()

print('Em que posição está o time do Flamengo? ', tupla.index('Flamengo') + 1)
print()


# FORMA ALTERNATIVA DE FAZER O EXERCÍCIO:

# print('-=-' * 40)
# print('{:^120}'.format('Os 5 primeiros colocados são:'))
# print('{:^120}'.format(f'{tupla[0:5]}'))
# print('-=-' * 40)
# print()

# print('-=-' * 40)
# print('{:^120}'.format('Os últimos 4 colocados são:'))
# print('{:^120}'.format(f'{tupla[16:]}')) # Poderia usar 'tupla[-4:]' também.
# print('-=-' * 40)
# print()

# print('-=-' * 40)
# print('{:^120}'.format('Em ordem alfabética:'))
# print('{:^120}'.format(f'{sorted(tupla[:7])}'))
# print('{:^120}'.format(f'{sorted(tupla[6:13])}'))
# print('{:^120}'.format(f'{sorted(tupla[12:])}'))
# print('-=-' * 40)
# print()

# print('-=-' * 40)
# print('{:^120}'.format(f'O time do Flamengo está na posição: {tupla.index("Flamengo") + 1}'))
# print('-=-' * 40)
# print()
