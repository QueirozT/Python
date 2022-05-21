print('===== DESAFIO #083 =====')
print()

valor = input('Digite uma expressão matemática: ')

abertura = valor.count('(')
fechamento = valor.count(')')

if abertura == fechamento:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
print()
