# TESTANDO UMA FUNÇÃO QUE CRIA UM LOOP E VERIFICA SE UM VALOR DIGITADO É INTEIRO.
def inputInt(txt):
    """
    -> Esta função coleta e verifica se o valor digitado é inteiro.
    :txt = Texto exibido na coleta do valor.
    #Criado por Tiago 
    """
    while True:
        val = input(txt)
        if val.isnumeric():
            break
        else:
            print('Valor Incorreto.')
    return val

valor = inputInt('Digite um valor: ')
print(f'O valor digitado foi {valor}')

# TESTANDO FORMAS DE VISUALIZAR A DOCSTRING DE UMA FUNÇÃO.
help(inputInt)
print(inputInt.__doc__)
