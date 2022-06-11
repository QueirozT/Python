# Criando funções para manipular arquivos json.
import json # Importando o módulo json.


def perguntas_json(local):
    """
    Esta função abre um arquivo json e retorna um dicionário com as perguntas e respostas.
    - local: Local do arquivo json.
    - return: Retorna um dicionário com as informações do arquivo.
    """
    listaDePerguntas = dict()  # Criando um dicionário para armazenar as perguntas e respostas.

    try:
        with open(local, 'r') as arquivo:  # Tentando carregar o arquivo.json
            listaDePerguntas = json.load(arquivo)  # Tentando converter o arquivo.json em dicionário.
    except:
        with open(local, 'w+'):  # Criando um arquivo.json vazio - Erro na abertura ou leitura.
            pass

    return listaDePerguntas


def escrever_json(local, perguntas):
    """
    Esta função escreve as perguntas em um arquivo json, caso o arquivo ainda não exista ele será criado.
    Caso já existam dados no arquivo, a função mescla os valores dos dicionários e atualiza o arquivo.
    Se os dados informados forem identicos aos existentes, a função não faz nada.
    - local: Local do arquivo.json
    - perguntas: Dicionário com as perguntas e respostas que serão escritas no arquivo.
    - return: None
    """
    temporario = dict()  # Criando um dicionário temporário para armazenar os valores do arquivo.
    
    try:
        with open(local, 'r') as file: # Tentando abrir o arquivo json para coletar valores existentes.
            temporario = json.load(file)  # Tentando Converter o arquivo json em um dicionário.
    except:
        with open(local, 'w+') as file: # Criando um arquivo.json novo e vazio - Erro na abertura ou leitura.
            pass
    finally:
        with open(local, 'w') as file: # Abrindo o arquivo json para escrever os valores.
            temporario.update(perguntas)  # Atualizando o dicionário temporário com todas as perguntas e respostas.
            file.write(json.dumps(temporario, indent=True))  # Escrevendo o dicionário no arquivo json com identação personalizada.
