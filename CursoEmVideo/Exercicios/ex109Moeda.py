def moeda(val=0, moeda='R$'):
    return f'{moeda}{val:.2f}'.replace('.', ',')


def metade(val=0, show=False):
    resp = val / 2
    return resp if not show else moeda(resp)


def dobro(val=0, show=False):
    resp = val * 2
    return resp if not show else moeda(resp)


def aumentar(val=0, porc=0, show=False):
    resp = val + (val * porc / 100)
    return resp if not show else moeda(resp)


def diminuir(val=0, porc=0, show=False):
    resp = val - (val * porc / 100)
    return resp if not show else moeda(resp)
