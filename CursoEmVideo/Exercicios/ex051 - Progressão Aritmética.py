print('===== EXERCÍCIO #51 =====')
print()

valor = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
print()

print('Os 10 primeiros valores de uma PA de razão {} começando de {} são:'.format(razao, valor))
for i in range(0, 10):
    print('{:>3}° = {}'.format(i+1, valor))
    valor += razao
print()
