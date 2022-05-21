print('===== DESAFIO #083 =====')
print()

valor = input('Digite uma expressão matemática: ')

abertura = valor.count('(') # Conta quantas vezes aparece o caractere '('
fechamento = valor.count(')') # Conta quantas vezes aparece o caractere ')'

if abertura == fechamento and valor.find('(') < valor.find(')'): # Verifica qual apareceu primeiro e se a quantidade de ambos é a mesma.
    print('Expressão válida!')
else:
    print('Expressão inválida!')
print()



# VERSÃO ALTERNATIVA:

# expr = input('Digite uma expressão matemática: ')
# pilha = []

# for i in expr: # Percorre a string e contabiliza se o caractere de abertura e fechamento estão na posição certa.
#     if i == '(':
#         pilha.append('(')
#     elif i == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break

# if len(pilha) == 0: # Verifica se a pilha está vazia. Se estiver, a expressão é válida.
#     print('Expressão válida!')
# else:
#     print('Expressão inválida!')
# print()
