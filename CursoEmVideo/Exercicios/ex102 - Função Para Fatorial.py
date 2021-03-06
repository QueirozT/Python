print('===== EXERCÍCIO #102 =====')
print()


def fatorial(num, show=False): # Definindo a função com o parâmetro (Opcional) show como False.
    """
    -> Calcula o fatorial de um número.
    : num = o número a ser calculado.
    : show = (opcional) mostra ou não a conta.
    : return: o valor do fatorial de um número.
    # Criada por Tiago.
    """
    fat = 1
    calc = ''

    for i in range(num, 0, -1):
        fat *= i
        
        if i == num:
            calc += f'{i}'
        else:
            calc += f' x {i}'
    
    if show:
        return f'{calc} = {fat}'
    else:
        return fat


# Programa Principal
valor = int(input('Qual o valor que deseja descobrir o fatorial? ')) # Solicitando o valor a ser calculado.

while True:
    opcao = str(input('Deseja mostrar o processo de cálculo? [S/N] ')).upper().strip()[0] # Verificando se quer ver os cálculos.
    if opcao in 'SN':
        break
    print('ERRO! Digite apenas S ou N.')
if opcao == 'S':
    show = True
else:
    show = False

print(fatorial(valor, show)) # Chamando a função e exibindo o resultado.
print()

help(fatorial) # Exibindo a documentação da função (DocString).



# Forma alternativa de criar uma função com parâmetros opcionais.


# def fatorial(n, show=False):
#     """
#     -> Calcula o fatorial de um número.
#     : n = o número a ser calculado.
#     : show = (opcional) mostra ou não a conta.
#     : return: o valor do fatorial de um número.
#     # Criada por Tiago.
#     """
#     f = 1

#     for c in range(n, 0, -1):
#         if show:
#             print(c, 'x' if c > 1 else '=', end=' ')
#         f *= c

#     return f
