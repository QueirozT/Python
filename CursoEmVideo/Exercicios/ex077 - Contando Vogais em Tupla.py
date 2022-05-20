print('===== EXERCÍCIO #077 =====')
print()

tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for v in tupla: # Desta forma o item 'v' recebe o valor de cada elemento da tupla.
    print(f'Na palavra {v} temos: ', end='')
    
    for c in v: # Desta forma o item 'c' recebe o valor de cada caractere da palavra e verifica se é uma vogal.
        if c in 'AEIOU':
            print(c, end=' ')
    print()
    
print('\n')
