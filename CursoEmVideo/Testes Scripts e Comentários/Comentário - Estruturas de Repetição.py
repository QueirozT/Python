# ESTRUTURA DE REPETIÇÃO (FOR) OU "ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE" (for == para):

# O for é um laço de repetição que executa uma determinada ação para cada elemento de um iterável.

# o for é composto de 3 partes que são encontradas dentro do range():
# 1 - A variável de controle, que é iniciada com o valor inicial e incrementada ao final de cada repetição.
# 2 - O teste de condição, que é executado para cada repetição.
# 3 - A ação a ser executada (opcional).

# EXEMPLO 01: Contar de 0 a 9 (O valor padrão da variável de controle é "0", e não informei a ação. Posso colocar só o teste de condição.)
print('EXEMPLO 01: Contar de 0 a 9.')
for i in range(10):
    print('{:^10}'.format(i))
print('=' * 10)

# EXEMPLO 02: Contar de 0 a '8' de 2 em 2 (ele não conta o ultimo digito, por isso de 0 a "8" e não "10")
print('EXEMPLO 02: Contar de 0 a 8 de 2 em 2.')
for i in range(0, 10, 2):
    print('{:^10}'.format(i))
print('=' * 10)

# EXEMPLO 03: Contar de 10 a 0 só que de trás para frente
print('EXEMPLO 03: Contar de 10 a 0.')
for i in range(10, -1, -1):
    print('{:^10}'.format(i))
print('=' * 10)


# O for também pode ser utilizado para ler estruturas compostas como tuplas, listas e dicionários.
# EXEMPLO 04: Mostrar todos os valores de uma tupla
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('EXEMPLO 04: Mostrar todos os valores de uma tupla')
for i in tupla:
    print('{:^10}'.format(f'{i}'))



# ===========================================================================================

# ESTRUTURA DE REPETIÇÃO (WHILE) OU "ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO" (while == enquanto):

# O while é um laço de repetição que executa um determinado bloco de código enquanto uma determinada condição for verdadeira.

# O while é composto de 2 partes:
# 1 - O teste de condição.
# 2 - O bloco de código a ser executado.

# EXEMPLO 01: Anotar um número enquanto o valor for maior que 0
print('EXEMPLO 01: Anotar um número enquanto o valor for maior que 0')
valor = 1
while valor != 0:
    valor = int(input('Digite um número: '))
print('Fim')

# EXEMPLO 02: Anotar um valor e perguntar se quer continuar ou não
print('EXEMPLO 02: Anotar um valor e perguntar se quer continuar ou não')
resp = 'S'
while resp == 'S':
    valor = int(input('Digite um número: '))
    resp = input('Quer continuar? [S/N] ').upper().strip()
print('Fim')



# ESTRUTURA DE REPETIÇÃO (INFINITA) OU "ESTRUTURA DE REPETIÇÃO DO-WHILE":

# O Do-While não existe no Python, mas pode ser replicado utilizando uma estrutura infinita "while" com uma condicional 'break'

# EXEMPLO 03: Anotar um número enquanto o valor for maior que 0
print('EXEMPLO 03: Anotar um número enquanto o valor for maior que 0 (Do-While)')
while True:
    valor = int(input('Digite um número: '))
    if valor == 0:
        break
print('Fim')


# EXEMPLO 04: Anotar um valor e perguntar se quer continuar ou não
print('EXEMPLO 04: Anotar um valor e perguntar se quer continuar ou não (Do-While)')
while True:
    valor = int(input('Digite um número: '))
    resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break
print('Fim')
