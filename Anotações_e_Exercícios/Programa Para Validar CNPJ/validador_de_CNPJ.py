def validarCNPJ(CNPJ):
    """
    Esta função Valida o CNPJ informado pelo usuário e retorna um valor booleano indicando se o CNPJ é válido ou não.
    - Para validar o CNPJ o algoritmo precisa gerar os dois ultimos dígitos e comparar com o valor informado.
        * Para gerar o penultimo dígito: 
            Deve multiplicar os 12 dígitos do CNPJ pela sequência "5432987665432" e somar todos os resultados. 
            Depois aplicar a fórmula: 11 - (resultado % 11) if > 9 else resultado.
        * Para gerar o ultimo dígito:
            Deve multiplicar os 13 dígitos do CNPJ pela sequência "6543298765432" e somar todos os resultados.
            Depois aplicar a fórmula: 11 - (resultado % 11) if > 9 else resultado.
    - CNPJ: Valor a ser validado.
    - return: True se o CNPJ for válido e False se o CNPJ for inválido
    """
    if len(CNPJ) != 14 or CNPJ == '0' * 14:  # Verifica se o CNPJ é válido
        return False

    CNPJ = [int(v) for v in CNPJ]  # Cria uma lista de inteiros
    NOVO_CNPJ = CNPJ[0:12]  # Cria uma lista com os 12 primeiros dígitos do CNPJ

    for i in range(25):
        if i == 0 or i == 12:
            soma = 0
            c = 5 if i == 0 else 6
        if c == 1:
            c = 9
        if i < 12:  # Primeiro loop para multiplicar os 12 dígitos do CNPJ pelas sequências "543298765432"
            soma += NOVO_CNPJ[i] * c
            if i == 11:
                NOVO_CNPJ.append(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))  # Aplica a fórmula e retorna o penultimo dígito do CNPJ
        else:  # Segundo loop para multiplicar os 13 dígitos do CNPJ pelas sequências "6543298765432"
            soma += c * NOVO_CNPJ[i-12]
            if i == 24:
                NOVO_CNPJ.append(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))  # Aplica a fórmula e retorna o último dígito do CNPJ
        c -= 1

    if NOVO_CNPJ == CNPJ:
        return True
    return False


def alternativo_ValidaCNPJ(valor):
    if len(valor) != 14 or valor == '0' * 14:
        return False

    valor = [int(v) for v in valor]  # Cria uma lista de inteiros
    CNPJ  = valor[0:12]  # Cria uma lista com os 12 primeiros dígitos do CNPJ
    
    for i in range(12):  # Calcula o valor do penultimo dígito do CNPJ "543298765432"
        if i == 0:
            soma = 0
            c = 5
        if c == 1:
            c = 9
        soma += c * CNPJ[i]
        c -= 1
    CNPJ.append(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))  # Aplica a fórmula e retorna o penultimo dígito do CNPJ

    for i in range(13):  # Calcula o valor do último digito do CNPJ "6543298765432"
        if i == 0:
            soma = 0
            c = 6
        if c == 1:
            c = 9
        soma += c * CNPJ[i]
        c -= 1
    CNPJ.append(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))  # Aplica a fórmula e retorna o último dígito do CNPJ

    if CNPJ == valor:
        return True
    return False


def recebe_cnpj(msg):
    """
    Recebe o CNPJ do usuário e remove os caracteres especiais
    - msg: Mensagem a ser exibida para o usuário
    - return: Os 14 dígitos do CNPJ digitado pelo usuário
    """
    while True:
        try:
            valor = input(msg).replace('.', '').replace('/', '').replace('-', '')
            if len(valor) != 14:
                raise ValueError
        except:
            print('CNPJ Inválido!')
            continue
        else:
            return valor


def formata_cnpj(val):
    """
    Formata o CNPJ para o formato: 00.000.000/0000-00
    - val: CNPJ a ser formatado
    - return: CNPJ formatado
    """
    if len(val) == 14:
        return f'{valor[0:2]}.{valor[2:5]}.{valor[5:8]}/{valor[8:12]}-{valor[12:14]}'
    return None


if __name__ == '__main__':
    valor = recebe_cnpj('\nDigite um CNPJ: ')  # Recebe o CNPJ do usuário

    print(f'\nO CNPJ: {formata_cnpj(valor)} é {"Válido!" if validarCNPJ(valor) else "Inválido!"}')
    
    print(f'\nO CNPJ: {formata_cnpj(valor)} é {"Válido!" if alternativo_ValidaCNPJ(valor) else "Inválido!"}\n')
