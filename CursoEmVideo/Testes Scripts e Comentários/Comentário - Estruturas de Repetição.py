# ESTRUTURA DE REPETIÇÃO (FOR) OU "ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE".

# O for é um laço de repetição que executa uma determinada ação para cada elemento de um iterável.

# o for é composto de 3 partes que são encontradas dentro do range():
# 1 - A variável de controle, que é iniciada com o valor inicial e incrementada ao final de cada repetição.
# 2 - O teste de condição, que é executado para cada repetição.
# 3 - A ação a ser executada (opcional).

# EXEMPLO 01: contar de 0 a 9 (O valor padrão da variável de controle é "0", e não informei a ação. Posso colocar só o teste de condição.)
for i in range(10):
    print('{:^10}'.format(i))
print('=' * 10)

# EXEMPLO 02: contar de 0 a '8' de 2 em 2 (ele não conta o ultimo digito, por isso de 0 a "8" e não "10")
for i in range(0, 10, 2):
    print('{:^10}'.format(i))
print('=' * 10)

# EXEMPLO 03: contar de 10 a 0 só que de trás para frente
for i in range(10, -1, -1):
    print('{:^10}'.format(i))
print('=' * 10)


# ===========================================================================================

# ESTRUTURA DE REPETIÇÃO (WHILE) OU "ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO"):

