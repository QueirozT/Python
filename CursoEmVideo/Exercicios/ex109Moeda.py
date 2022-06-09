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
