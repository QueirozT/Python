def validarCPF(list):
    """
    Função que recebe uma lista com os 11 digitos de um cpf e valida se é um cpf válido.
    - list: lista com os 11 digitos de um cpf
    - return: True se o cpf for válido, False se não for válido
    """
    if len(list) != 11:
        return False
    else:
        soma = 0
        for i, v in enumerate(range(10, 1, -1)):
            soma += list[i] * v
        
        digito = 0 if 11 - (soma % 11) > 9 else (11 - (soma % 11))  # Validando o penultimo digito
        
        soma = 0
        for i, v in enumerate(range(11, 1, -1)):
            soma += list[i] * v
        
        digito += 0 if 11 - (soma % 11) > 9 else (11 - (soma % 11))  # Validando o ultimo digito

        seq = (str(list[0]) * 11) == ''.join(str(x) for x in list)  # Verifica se os 11 digitos são sequenciais.

        if digito == list[9] + list[10] and not seq: # Verificando se a soma dos dois ultimos digitos são iguais aos validados.
            return True
        else:
            return False


def validadorAlternativo(list):
    """
    Função que recebe uma lista com os 11 digitos de um cpf e valida se é um cpf válido.
    - list: lista com os 11 digitos de um cpf
    - return: True se o cpf for válido, False se não for válido
    """
    if len(list) != 11:
        return False
    else:
        soma = 0
        for i in range(10):
            soma += list[i] * (11 - i)

        resto = soma % 11

        if resto < 2:
            resto = 0
        else:
            resto = 11 - resto

        seq = (str(list[0]) * 11) == ''.join(str(x) for x in list)  # Verifica se os 11 digitos são sequenciais.

        if resto == list[10] and not seq:
            return True
        else:
            return False


def recebe_cpf(txt):
    """
    Função que coleta um cpf do usuário e retorna uma lista com os 11 digitos do cpf.
    - txt: texto que será exibido para o usuário
    - return: lista com os 11 digitos do cpf
    """
    list = []

    while True:
        val = input(txt).strip().replace('.', '').replace('-', '').replace(' ', '')
        
        if len(val) != 11 or not val.isdigit():
            print('CPF inválido')
        else:
            for i in val:
                list.append(int(i))
            return list


def msg(txt):
    """
    Função que exibe uma mensagem centralizada entre duas linhas.
    - txt: texto que será formatado
    - return: Mensagem formatada
    """
    print('-' * (len(txt) + 10))
    print(txt.center(len(txt) + 10))
    print('-' * (len(txt) + 10))
