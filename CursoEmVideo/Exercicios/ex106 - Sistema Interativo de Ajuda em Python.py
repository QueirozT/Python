from time import sleep

print('===== EXERCÍCIO #106 =====')
print()


def msg(txt, cor='\033[m'):
    """
    -> Função para formatar uma mensagem e mostrar na tela.
    :txt = Mensagem a ser formatada.
    :cor = (Opcional) Cor da mensagem, padrão é nenhuma cor.
    :return: Sem retorno, imprime a mensagem formatada.
    # Criado por Tiago.
    """
    print(cor + '~' * (len(txt) + 10) + '\033[m')
    print(cor + f'{txt:^{len(txt) + 10}}' + '\033[m')
    print(cor + '~' * (len(txt) + 10) + '\033[m')
    print()


# Programa Principal.
while True:
    # Exibindo o menu.
    msg('SISTEMA DE AJUDA PyHELP', '\033[0;43m')

    # Coletando o nome da função ou biblioteca.
    nome = str(input('Função ou Biblioteca > '))
    print()

    # Verificando se o usuário quer sair do programa.
    if nome.upper() in 'FIM SAIR':
        break

    # Mensagem de carregamento.
    msg(f'Acessando o manual do comando: {nome}', '\033[0;44m')
    sleep(2)

    # Área de impressão do manual.
    print('\033[7;40m')
    help(nome)
    print('\033[m')
