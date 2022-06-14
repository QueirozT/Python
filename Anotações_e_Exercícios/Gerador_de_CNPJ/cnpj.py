def gerarCNPJ():
    """
    Esta função aplica os conceitos de validação de um CNPJ para gerar os ultimos dígitos de uma sequência randômica de CNPJ.
    - Para gerar o penultimo dígito:
        Deve multiplicar os 12 dígitos do CNPJ pela sequência "5432987665432" e somar todos os resultados.
        Depois aplicar a fórmula: if (11 - (resultado % 11)) > 9 else 0.
    - Para gerar o ultimo dígito:
        Deve multiplicar os 13 dígitos do CNPJ pela sequência "5432987665432" e somar todos os resultados.
        Depois aplicar a fórmula: if (11 - (resultado % 11)) > 9 else 0.
    - return: CNPJ randômico válido e formatado.
    """
    from random import randint
    cnpj = [int(v) for v in str(randint(00000000, 99999999)) + '0001']  # Gerando os 12 primeiros digitos do CNPJ aleatóriamente
    REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]  # "CONSTANTE" para aplicar a fórmula de validação do CNPJ

    # Aplicando a formula para calcular o penultimo digito do CNPJ e adicionando ao CNPJ
    penultimo = 11 - (sum([cnpj[i] * v for i, v in enumerate(REGRESSIVOS[1:])]) % 11)
    cnpj.append(0 if penultimo > 9 else penultimo)  # Verificando e adicionando o penultimo digito do CNPJ

    # Aplicando a formula para calcular o ultimo digito do CNPJ e adicionando ao CNPJ
    ultimo = 11 - (sum([cnpj[i] * v for i, v in enumerate(REGRESSIVOS)]) % 11)
    cnpj.append(0 if ultimo > 9 else ultimo)  # Verificando e adicionando o ultimo digito do CNPJ
    
    return formata_CNPJ(cnpj)


def formata_CNPJ(val):
    """
    Função que formata um CNPJ para o formato 00.000.000/0000-00
    - val: valor a ser formatado.
    - return: valor formatado (String)
    """
    if type(val) == list:  # Verificando se o valor é uma lista
        val = ''.join(str(v) for v in val)  # Convertendo a lista em string
    elif type(val) == int:  # Verificando se o valor é um inteiro
        val = str(val)  # Convertendo o inteiro em string
    
    return f'{val[0:2]}.{val[2:5]}.{val[5:8]}/{val[8:12]}-{val[12:14]}'



if __name__ == '__main__':  # Área de testes: Este bloco não é executado se o módulo for importado por outro programa.
    print(f'\nTestando a função formata_CNPJ(): {formata_CNPJ(12345678901234)}')

    print(f'\nCNPJ Válido: {gerarCNPJ()}\n')
