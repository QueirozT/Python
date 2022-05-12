print('===== EXERCÍCIO #51 =====')
print()

print('=-=' * 20)
print('{:^60}'.format('10 TERMOS DE UMA PA - PROGRESSÃO ARITMÉTICA'))
print('=-=' * 20)

termo = int(input('Primeiro Termo? '))
razao = int(input('Razão? '))
print()

for c in range(0, 10):
    print('{}'.format(termo), end=' → ')
    termo += razao
print('ACABOU!')
print()


# VERSÃO ALTERNATIVA DO PROGRAMA.

# valor = int(input('Digite um número: '))
# razao = int(input('Digite a razão: '))
# print()

# print('Os 10 primeiros valores de uma PA de razão {} começando de {} são:'.format(razao, valor))
# for i in range(0, 10):
#     print('{:>3}° = {}'.format(i+1, valor))
#     valor += razao
# print()
