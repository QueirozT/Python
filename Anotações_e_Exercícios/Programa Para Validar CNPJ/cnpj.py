def validarCNPJ(cnpj):
    """
    Esta função Valida o CNPJ informado pelo usuário e retorna um valor booleano indicando se o CNPJ é válido ou não.
    - Para validar o CNPJ o algoritmo precisa gerar os dois ultimos dígitos e comparar com o valor informado.
        * Para gerar o penultimo dígito: 
            Deve multiplicar os 12 dígitos do CNPJ pela sequência "5432987665432" e somar todos os resultados. 
            Depois aplicar a fórmula: 11 - (resultado % 11) if > 9 else resultado.
        * Para gerar o ultimo dígito:
            Deve multiplicar os 13 dígitos do CNPJ pela sequência "6543298765432" e somar todos os resultados.
            Depois aplicar a fórmula: 11 - (resultado % 11) if > 9 else resultado.
    - cnpj: Valor a ser validado.
    - return: True se o CNPJ for válido e False se o CNPJ for inválido
    """
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:  # Verifica se um CNPJ foi informado e se é um sequêncial.
        return False

    cnpj = [int(v) for v in cnpj]  # Cria uma lista de inteiros
    novo_cnpj = cnpj[0:12]  # Cria uma lista com os 12 primeiros dígitos do CNPJ

    for i in range(25):
        if i == 0 or i == 12:
            soma = 0
            c = 5 if i == 0 else 6
        if c == 1:
            c = 9
        if i < 12:  # Primeiro loop para multiplicar os 12 dígitos do CNPJ pelas sequências "543298765432"
            soma += novo_cnpj[i] * c
            if i == 11:
                novo_cnpj.append(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))  # Aplica a fórmula e retorna o penultimo dígito do CNPJ
        else:  # Segundo loop para multiplicar os 13 dígitos do CNPJ pelas sequências "6543298765432"
            soma += c * novo_cnpj[i-12]
            if i == 24:
                novo_cnpj.append(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))  # Aplica a fórmula e retorna o último dígito do CNPJ
        c -= 1

    if novo_cnpj == cnpj:
        return True
    return False


def alternativo_ValidarCNPJ(valor):
    """
    Esta função aplica a formula de validação de CNPJ e retorna um valor booleano indicando se o CNPJ é válido ou não.
    - Para validar o CNPJ o algoritmo precisa gerar os dois ultimos dígitos e comparar com o valor informado.
        * Para gerar o penultimo dígito:
            Deve multiplicar os 12 dígitos do CNPJ pela sequência "5432987665432" e somar todos os resultados.
            Depois aplicar a fórmula: if (11 - (resultado % 11)) > 9 else 0.
        * Para gerar o ultimo dígito:
            Deve multiplicar os 13 dígitos do CNPJ pela sequência "6543298765432" e somar todos os resultados.
            Depois aplicar a fórmula: if (11 - (resultado % 11)) > 9 else 0.
    - valor: Valor a ser validado.
    - return: True se o CNPJ for válido e False se o CNPJ for inválido
    """
    if len(valor) != 14 or valor == valor[0] * 14:
        return False

    valor = [int(v) for v in valor]  # Cria uma lista de inteiros
    cnpj  = valor[0:12]  # Cria uma lista com os 12 primeiros dígitos do CNPJ
    REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]  # Criando uma "Constante" para os regressivos
    
    # Aplicando a formula de validação do CNPJ para a multiplicação dos 12 primeiros dígitos do CNPJ pelos 12 dígitos REGRESSIVOS
    penultimo = 11 - (sum([cnpj[i] * v for i, v in enumerate(REGRESSIVOS[1:])]) % 11)
    penultimo = 0 if penultimo > 9 else penultimo  # Verifica se o penultimo dígito é maior que 9 e se for, o dígito é 0
    cnpj.append(penultimo)  # Adiciona o penultimo dígito ao CNPJ

    # Aplicando a formula de validação do CNPJ para a multiplicação dos 13 dígitos do CNPJ pelos 13 dígitos REGRESSIVOS
    ultimo = 11 - (sum([cnpj[i] * v for i, v in enumerate(REGRESSIVOS)]) % 11)
    ultimo = 0 if ultimo > 9 else ultimo  # Verifica se o ultimo dígito é maior que 9 e se for, o dígito é 0
    cnpj.append(ultimo)  # Adiciona o ultimo dígito ao CNPJ

    # Verifica se o CNPJ gerado pela formula é o mesmo que o CNPJ informado pelo usuário
    if cnpj == valor:
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
    
    print(f'\nO CNPJ: {formata_cnpj(valor)} é {"Válido!" if alternativo_ValidarCNPJ(valor) else "Inválido!"}\n')
