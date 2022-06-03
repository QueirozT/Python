from ex115.lib.interface import * # Importando as funções da interface para utilizar nos arquivos.


def arquivoExiste(nome):
    """
    -> Criando uma função que tenta abrir um arquivo de texto e verifica se ele existe.
    :nome = nome do arquivo.
    :return: retorna True se o arquivo existir, False se não existir.
    """
    try:
        a = open(nome, 'rt') # Tentando abrir um arquivo de texto com os parâmetros "rt" Read Text.
        a.close()
    except:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    -> Função que tenta abrir um arquivo, e caso ele não exista cria um.
    :nome = nome do arquivo.
    :return: um arquivo novo.
    """
    try:
        a = open(nome, 'wt+') # Tentando abrir um arquivo de texto com os parâmetros "wt" Write Text e caso não exista cria um "+".
        a.close()
    except:
        print('Houve um erro ao criar o arquivo.')
    else:
        print(f'Arquivo "{nome}" criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt') # Tentando abrir um arquivo de texto com os parâmetros "rt" Read Text.
    except:
        print('Falha ao ler o arquivo.')
    else:
        msg('PESSOAS CADASTRADAS')
        print(a.read()) # Mostrando tudo que está dentro do arquivo.
    finally:
        a.close() # fechando o arquivo.
