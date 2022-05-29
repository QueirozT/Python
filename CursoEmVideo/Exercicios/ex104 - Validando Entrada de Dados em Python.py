print('===== EXERCÍCIO #104 =====')
print()


def lerInt(txt):
    """
    -> Função para ler um valor inteiro.
    :txt = Texto a ser exibido para o usuário.
    :return: Valor inteiro.
    """
    while True:
        num = input(txt)
        if num.isnumeric():
            break
        print('\033[31mERRO! Digite um número válido!\033[m')

    return int(num)


# Programa Principal
n = lerInt('Digite um número: ')
print(F'Você digitou o número {n}')
print()
