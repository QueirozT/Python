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

print('Saindo do programa...')
print()



# PROGRAMA ALTERNATIVO:
# c = (
#     '\033[m', # 0 - Sem cor
#     '\033[0;41m', # 1 - vermelho 
#     '\033[0;43m', # 2 - amarelo
#     '\033[0;44m', # 3 - azul
#     '\033[7;40m', # 4 - brando
#     )

# def ajuda(com):
#     título(f'Acessando o manual do comando \'{com}\'', 3) # As \' são necessárias para adicionar as áspas.
#     print(c[4])
#     help(com)
#     print(c[0])
#     sleep(2)

# def título(msg, cor=0):
#     tam = len(msg) + 4
#     print(c[cor])
#     print('~' * tam)
#     print(f'  {msg}')
#     print('~' * tam)
#     print(c[0])
#     sleep(1)


# # Programa Principal
# while True:
#     título('SISTEMA DE AJUDA PyHELP', 2)
#     comando = str(input('Função ou Biblioteca > '))
#     if comando.upper() == 'FIM':
#         break
#     else:
#         ajuda(comando)
# título('Até logo!', 1)
