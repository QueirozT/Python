print('===== EXERCÍCIO #51 =====')
print()

print('=-=' * 20)
print('{:^60}'.format('10 TERMOS DE UMA PA - PROGRESSÃO ARITMÉTICA'))
print('=-=' * 20)

termo = int(input('Primeiro Termo? '))
razao = int(input('Razão? '))
print()

decimo = termo + (10 - 1) * razao # Fórmula matemática para identificar o 10° termos de uma PA.

for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end=' → ')
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
