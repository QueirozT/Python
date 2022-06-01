def moeda(val=0, moeda='R$'):
    """
    -> Função para formatar moeda
    :val = Valor a ser formatado
    :moeda = Tipo de moeda
    :return: Retorna o valor formatado
    # Criado por: Tiago.
    """
    return f'{moeda}{val:.2f}'.replace('.', ',')


def metade(val=0, show=False):
    """
    -> Função para calcular a metade de um valor
    :val = Valor a ser calculado
    :show = Mostrar ou não o valor formatado com a função moeda().
    :return: Retorna o valor calculado.
    # Criado por: Tiago.
    """
    resp = val / 2
    return resp if not show else moeda(resp)


def dobro(val=0, show=False):
    """
    -> Função para calcular o dobro de um valor
    :val = Valor a ser calculado
    :show = Mostrar ou não o valor formatado com a função moeda().
    :return: Retorna o valor calculado.
    # Criado por: Tiago.
    """
    resp = val * 2
    return resp if not show else moeda(resp)


def aumentar(val=0, porc=0, show=False):
    """
    -> Função para aumentar um valor em porcentagem
    :val = Valor a ser calculado
    :porc = Porcentagem a ser calculada
    :show = Mostrar ou não o valor formatado com a função moeda().
    :return: Retorna o valor calculado.
    # Criado por: Tiago.
    """
    resp = val + (val * porc / 100)
    return resp if not show else moeda(resp)


def diminuir(val=0, porc=0, show=False):
    """
    -> Função para diminuir um valor em porcentagem
    :val = Valor a ser calculado
    :porc = Porcentagem a ser calculada
    :show = Mostrar ou não o valor formatado com a função moeda().
    :return: Retorna o valor calculado.
    # Criado por: Tiago.
    """
    resp = val - (val * porc / 100)
    return resp if not show else moeda(resp)


def resumo(val=0, porc1=10, porc2=5):
    """
    -> Função que retorna o resumo formatado de um valor
    :val = Valor a ser calculado
    :porc1 = (Opcional) Porcentagem de aumento a ser calculada
    :porc2 = (Opcional) Porcentagem de decremento a ser calculada
    :return: Retorna o resumo formatado.
    # Criado por: Tiago.
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30)) # Função do print() que centraliza um texto.
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(val)}')
    print(f'Dobro do preço: \t{dobro(val, True)}')
    print(f'Metade do preço: \t{metade(val, True)}')
    print(f'{porc1}% de aumento: \t{aumentar(val, porc1, True)}')
    print(f'{porc2}% de redução: \t{diminuir(val, porc2, True)}')
    print('-' * 30)
