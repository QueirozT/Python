def converte(tamanho):
    """
    Função que converte de bytes para M, G, etc.

    Esta função recebe um tamanho em bytes e converte o valor utilizando a base 1024 retornando o valor convertido em K, M, G, etc.
    """
    base = 1024
    if tamanho < base:
        return f'{tamanho}B ({tamanho}bytes)'
    elif tamanho < base ** 2:
        return f'{tamanho / base:.2f}KB ({tamanho} bytes)'
    elif tamanho < base ** 3:
        return f'{tamanho / base ** 2:.2f}MB ({tamanho} bytes)'
    elif tamanho < base ** 4:
        return f'{tamanho / base ** 3:.2f}GB ({tamanho} bytes)'
    elif tamanho < base ** 5:
        return f'{tamanho / base ** 4:.2f}TB ({tamanho} bytes)'


def cor(num):
    """
    Função que retorna uma cor

    Esta função recebe um número e retorna uma cor de acordo com o número.

        Parametros:
            num: Número da cor.
        
        Retorno:
            num = 0: Sem cor
            num = 1: Vermelho
            num = 2: Verde
            num = 3: Ciano
            num = 4: Azul
    """
    if num == 0:
        return '\033[m'
    if num == 1:
        return '\033[31m'
    elif num == 2:
        return '\033[32m'
    elif num == 3:
        return '\033[36m'
    elif num == 4:
        return '\033[34m'
    else:
        raise ValueError('Cor não encontrada!')
