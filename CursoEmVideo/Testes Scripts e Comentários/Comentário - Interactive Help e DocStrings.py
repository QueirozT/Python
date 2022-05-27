# Interactive Help: É um comando que mostra ajuda para o usuário.

# Como utilizar? 
# Existem duas formas de utilizar o Interactive Help:
# 1 - Utilizando a função help(comando) para exibir ajuda para um comando específico.
# 2 - Digitando help() no console para exibir ajuda para todos os comandos disponíveis.

#=======================================================================================================================


# DocStrings: É um comentário que é utilizado para documentar o código.

# Como utilizar?
# Para usar uma DocString, é só utilizar um print do comando seguido de .__doc__ EX: print(input.__doc__) para exibir a DocString.

# Como Criar uma DocString?
# As DocStrings servem para documentar o código, e também para explicar como o código funciona.
# Para criar, após definir a função "def", basta abrir 3 áspas duplas """ e escrever a DocString. depois fechar""".
# EX: Criando uma DocString para uma função contador.
def contador(i, f, p):
    """
    Função que mostra a contagem na tela.
    parâmetros:
    i = Início: Valor inicial da contagem.
    f = Fim: Valor do final da contagem.
    p = Passo: Valor do passo da contagem.
    Função criada por Tiago.
    """
    for valor in range(i, f+1, p):
        print(valor, end=', ')
    print('FIM!')


# Chamando a DocString Criada a cima.
print(contador.__doc__)
