def menu(list):
    """
    -> Função que cria um menu, valida e retornar a opção selecionada.
    :param list: lista com os itens do menu.
    :return: retorna a opção selecionada pelo usuário.
    """
    while True:
        msg('MENU PRINCIPAL')
        for i, opcao in enumerate(list):
            print(f'{cor(4)}{i+1} - {cor(7)}{opcao}{cor(0)}')
        linha()
        opcao = tamLista(f'Sua Opção: ', len(list))
        return opcao


def tamLista(msg='', tam=0):
    """
    -> Função para ler e validar um valor inteiro dentro de um intervalo.
    :msg = mensagem a ser exibida para o usuário.
    :tam = tamanho do intervalo.
    :return: retorna o valor inteiro validado.
    """
    while True:
        val = lerInt(msg)
        
        if val > tam or val <= 0:
            print(f'{cor(2)}Erro! Digite uma opção válida.{cor(0)}')
        else:
            return val


def lerInt(msg):
    """
    -> Função para ler e validar um valor inteiro.
    :msg = mensagem a ser exibida para o usuário.
    :return: retorna o valor inteiro validado.
    """
    while True:
        try:
            valor = int(input(f'{cor(4)}{msg}{cor(3)}'))
            print(f'{cor(0)}', end='')
        except KeyboardInterrupt:
            print(f'{cor(2)}O usuário preferiu não informar a opção...{cor(0)}')
            return 3
        except:
            print(f'{cor(2)}Erro! Por favor, digite um número inteiro válido.{cor(0)}')
        else:
            return valor


def linha(tam=60):
    """
    -> Função para criar uma linha.
    :tam = tamanho da linha (OPCIONAL).
    :return: retorna uma linha com o tamanho informado.
    """
    print('-' * tam)


def msg(msg, color=0):
    """
    -> Função para exibir uma mensagem formatada.
    :msg = mensagem a ser exibida.
    :color = a cor da mensagem (OPCIONAL).
    :return: retorna a mensagem formatada.
    """
    linha()
    print(f"{cor(color)}{msg}{cor()}".center(60))
    linha()


def cor(num=0):
    """
    -> Função que retorna um código de cor.
    :num = número da cor.
    :0 - Sem estilo
    :1 - Branco
    :2 - Vermelho
    :3 - Verde
    :4 - Amarelo
    :5 - Azul
    :6 - Roxo
    :7 - Ciano
    :8 - Cinza
    :return: retorna o código da cor escolhida.
    """
    cores = (
        '\033[m', '\033[0;30m', '\033[0;31m', '\033[0;32m', '\033[0;33m', '\033[0;34m', '\033[0;35m', '\033[0;36m', '\033[0;37m')
    
    if num >= len(cores):
        return cores[0]
    
    return cores[num]
