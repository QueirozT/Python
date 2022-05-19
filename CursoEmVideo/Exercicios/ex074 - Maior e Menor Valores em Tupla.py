from random import randint

print('===== EXERCÍCIO #074 =====')
print()

tupla = ()

for i in range(4):
    valor = (randint(0, 10),)
    tupla += valor

print(f'Os valores sorteados foram: {tupla[0:]}')
print()

print(f'O maior valor sorteado foi {sorted(tupla)[-1]}')
print()

print(f'O menor valor sorteado foi {sorted(tupla)[0]}')
print()
