from random import randint


def gerarCPF():
    """
    Função que gera um cpf aleatório
    - return: valor formatado
    """
    digitos = str(randint(100000000, 999999999))  # Gerando os 9 primeiros digitos do cpf aleatóriamente
    soma = 0

    for i, v in enumerate(range(10, 1, -1)):  # Calculando a soma dos 9 primeiros digitos do cpf
        soma += int(digitos[i]) * v
    
    resto = 0 if 11 - (soma % 11) > 9 else (11 - (soma % 11))  # Validando o penultimo digito do cpf

    digitos += str(resto)  # Adicionando o digito validado ao cpf
    soma = 0

    for i, v in enumerate(range(11, 1, -1)):  # Calculando a soma dos 10 digitos do cpf
        soma += int(digitos[i]) * v

    resto = 0 if 11 - (soma % 11) > 9 else (11 - (soma % 11))  # Validando o ultimo digito
    
    digitos += str(resto)  # Adicionando o digito validado ao cpf

    return formatCPF(digitos)  # Retornando o cpf completo


def formatCPF(val):
    """
    Função que formata um cpf para o formato 000.000.000-00
    - val: valor a ser formatado (String)
    - return: valor formatado
    """
    return f'{val[0:3]}.{val[3:6]}.{val[6:9]}-{val[9:11]}'
