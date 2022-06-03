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


def criarArquivo(nome, local):
    """
    -> Função que tenta abrir um arquivo, e caso ele não exista cria um.
    :nome = nome do arquivo.
    :local = caminho do arquivo.
    :return: um arquivo novo.
    """
    try:
        a = open(local, 'wt+') # Tentando abrir um arquivo de texto com os parâmetros "wt" Write Text e caso não exista cria um "+".
        a.close()
    except:
        print('Houve um erro ao criar o arquivo.')
    else:
        print(f'Arquivo "{nome}" criado com sucesso!')


def lerArquivo(nome):
    """
    -> Função que abre um arquivo e mostra o conteúdo do mesmo.
    :nome = nome do arquivo.
    :return: o conteúdo do arquivo.
    """
    try:
        a = open(nome, 'rt') # Tentando abrir um arquivo de texto com os parâmetros "rt" Read Text.
    except:
        print('Falha ao ler o arquivo.')
    else:
        msg('PESSOAS CADASTRADAS')
        for lin in a: # Lendo o arquivo linha por linha.
            pessoa = lin.strip().split(';') # Separando o nome e a idade e armazenando em uma lista.
            pessoa[1].replace('\n', '') # Substituindo a quebra de linha "\n" por nada para tirar os espaços na hora da leitura.
            print(f'{"":>5}{pessoa[0]:<25}{pessoa[1]:>20} anos') # Mostrando o nome e idade da pessoa formatados com espaços.
    finally:
        a.close() # fechando o arquivo.


def cadastrar(arq, nome='', idade=0):
    """
    -> Função que recebe o local do arquivo um nome e uma idade e adiciona os dados ao arquivo.
    :arq = local do arquivo.
    :nome = nome da pessoa.
    :idade = idade da pessoa.
    :return: não há retorno.
    """
    
    if nome == '':
        nome = 'Desconhecido'
    
    try:
        a = open(arq, 'at') # Tentando abrir um arquivo de texto com os parâmetros "at" Append Text.
    except:
        print('Falha ao cadastrar a pessoa.')
    else:
        try:
            a.write(f'{nome};{idade}\n') # Escrevendo o nome e idade na ultima linha do arquivo e dando uma quebra de linha.
        except:
            print('Falha ao escrever o arquivo.')
        else:
            print(f'{cor(3)}Novo registro {nome} adicionado com sucesso!{cor()}')
            a.close()
