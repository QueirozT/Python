from random import randint

print('===== EXERCÍCIO #074 =====')
print()

tupla = ()

for i in range(5):
    valor = (randint(0, 10),) # O '(valor,)' é necessário para que o valor seja uma tupla.
    tupla += valor # Somente uma tupla pode ser concatenada com outra tupla.

print(f'Os valores sorteados foram: {tupla}')
print()

print(f'O maior valor sorteado foi {sorted(tupla)[-1]}')
print()

print(f'O menor valor sorteado foi {sorted(tupla)[0]}')
print()


# FORMA ALTERNATIVA DE FAZER O EXERCÍCIO:

# tupla = ()

# print('Os valores sorteados foram: ', end='')

# for i in range(5):
#     tupla += (randint(0, 10),)
#     print(tupla[i], end=' ')
# print('\n')

# print(f'O maior valor sorteado foi: {max(tupla)}')
# print()

# print(f'O menor valor sorteado foi: {min(tupla)}')
# print()
