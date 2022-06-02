print('===== EXERCÍCIO #113 =====')
print()

cor = ('\033[m', # 0 - Sem estilo
    '\033[31m', # 1 - Vermelho
    '\033[32m', # 2 - verde
    '\033[33m', # 3 - Amarelo
    '\033[36m',) # 4 - Ciano


def lerInt(msg):
    """
    -> Função para ler e validar se é um número inteiro.
    :msg = mensagem a ser exibida para o usuário.
    :return: retorna o valor inteiro digitado.
    # Criado por: Tiago.
    """
    while True:
        try:
            valor = int(input(f'{cor[4]}{msg}{cor[0]}'))
        except KeyboardInterrupt:
            print(f'{cor[3]}O usuário preferiu não informar o valor...{cor[0]}')
            return 0
        except:
            print(f'{cor[1]}Erro! Por favor, digite um número inteiro válido.{cor[0]}')
        else:
            return valor


def lerFloat(msg):
    """
    -> Função para ler e validar um valor real.
    :msg = mensagem a ser exibida para o usuário.
    :return: retorna o valor real digitado.
    # Criado por: Tiago.
    """
    while True:
        try:
            valor = float(input(f'{cor[4]}{msg}{cor[0]}'))
        except KeyboardInterrupt:
            print(f'{cor[3]}O usuário preferiu não informar o valor...{cor[0]}')
            return 0
        except:
            print(f'{cor[1]}Erro! Por favor, digite um número real válido.{cor[0]}')
        else:
            return valor


# Programa Principal
ValInt = lerInt('Digite um número inteiro: ')
print()

ValFloat = lerFloat('Digite um número real: ')
print()

print(f'{cor[2]}O valor inteiro digitado foi {ValInt} e o valor real foi {ValFloat:.1f}{cor[0]}')
print()
