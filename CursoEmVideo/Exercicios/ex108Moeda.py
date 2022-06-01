def moeda(val=0, moeda='R$'):
    return f'{moeda}{val:.2f}'.replace('.', ',')


def metade(val=0):
    resp = val / 2
    return resp


def dobro(val=0):
    resp = val * 2
    return resp


def aumentar(val=0, porc=0):
    resp = val + (val * porc / 100)
    return resp


def diminuir(val=0, porc=0):
    resp = val - (val * porc / 100)
    return resp
