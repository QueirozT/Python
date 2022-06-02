def leiaDinheiro(txt):
    """
    -> Função para ler e validar um valor monetário.
    :txt = Texto a ser exibido para o usuário.
    :return: Valor monetário.
    # Criado por: Tiago.
    """
    while True:
        valor = str(input(txt)).replace(',','.').strip()

        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO! "{valor}" não é um preço válido. Tente novamente.\033[m')
        else:
            return float(valor)
            break


def lerInt(txt):
    """
    -> Função para ler e validar um número inteiro.
    :txt = Texto a ser exibido para o usuário.
    :return: Valor inteiro.
    # Criado por: Tiago.
    """
    while True:
        num = input(txt)
        if num.isnumeric():
            break
        print('\033[31mERRO! Digite um número válido!\033[m')

    return int(num)
