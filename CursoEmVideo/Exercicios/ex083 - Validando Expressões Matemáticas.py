print('===== DESAFIO #083 =====')
print()

valor = input('Digite uma expressão matemática: ')

abertura = valor.count('(')
fechamento = valor.count(')')

if abertura == fechamento and valor.find('(') < valor.find(')'):
    print('Expressão válida!')
else:
    print('Expressão inválida!')
print()



# VERSÃO ALTERNATIVA:

# expr = input('Digite uma expressão matemática: ')
# pilha = []

# for i in expr:
#     if i == '(':
#         pilha.append('(')
#     elif i == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break

# if len(pilha) == 0:
#     print('Expressão válida!')
# else:
#     print('Expressão inválida!')
# print()
