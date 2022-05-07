# CONDICIONAL SIMPLES

if True:
    print('Verdadeiro')


# CONDICIONAL COMPOSTA COM DOIS OPERADORES

if True and False:
    print('Verdadeiro')
else:
    print('Falso')


# CONDICIONAL COMPOSTA COM TRES OPERADORES

if True and False or True:
    print('Verdadeiro')
else:
    print('Falso')


# CONDICIONAL SIMPLIFICADA ps: não existe condicional ternária no python

print('Verdadeiro' if True else 'Falso') # EXEMPLO 01

variavel = 'verdadeiro' if True else 'Falso' # EXEMPLO 02


# CONDICIONAL COMPLEXA

if True:
    print('Verdadeiro')
elif False:
    print('Falso')
else:
    print('Não sei')
