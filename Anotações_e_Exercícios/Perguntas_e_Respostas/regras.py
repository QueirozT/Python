from encodings import utf_8


def perguntas(arq):
    """
    Esta função abre um arquivo txt e retorna um dicionário com as perguntas e respostas.
    - arq: Local do arquivo txt.
    - return: Retorna um dicionário com as informações do arquivo.
    """
    listaDePerguntas = dict()
    
    try:
        arquivo = open(arq, 'rt')
    except Exception as erro:
        print(f'\nO Seguinte erro foi identificado: {erro.__class__}')
        print(f'\n DETALHES DO ERRO:\n{erro}\n')
    else:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                Perguntas = linha.split(';')
                
                pergunta, respostas, certa = Perguntas[1].split(',')
                
                pergunta = pergunta.split(':')
                respostas = respostas.split(':')
                certa = certa.split(':')

                respostas[1] = respostas[1].split('|')
                    
                for i, v in enumerate(respostas[1]):
                    respostas[1][i] = v.split('=')
                    respostas[1][i] = {respostas[1][i][0]: respostas[1][i][1]}

                listaDePerguntas[Perguntas[0]] = {pergunta[0]: pergunta[1], respostas[0]: respostas[1], certa[0]: certa[1]}

        arquivo.close()
        return listaDePerguntas
    finally:
        pass  # Palavra Reservada para mostrar que algo será acrescentado neste bloco futuramente.


def resposta(valor):
    """
    Esta função coleta o valor digitado pelo usuário e verifica se a resposta informada está correta.
    - valor: Valor do item atual na lista de perguntas e respostas.
    - return: True ou False se o usuário acertou ou não a resposta.
    """
    try:
        resp = input('Qual a resposta? ').strip().lower()
    except:
        return False
    else: 
        igual = False
        for i in valor['respostas']:
            for k, v in i.items():
                if k == valor.get('certa') and v == resp:  # Verificando se a resposta digitada é igual a resposta correta escrita.
                    igual = True

        return True if valor.get('certa') == resp or igual else False  # Verificando se o indice ou o valor corresponde a resposta correta.


def porcentagemAcerto(acertos, perguntas):
    """
    Esta função retorna uma estimativa de acertos do usuário.
    - acertos: Quantidade de acertos que o usuário teve
    - perguntas: Quantidade de perguntas
    - return: Uma estimativa baseada na quantidade de acertos por pergunta.
    """
    return f'Total de perguntas: {len(perguntas)} \nAcertos: {acertos} \nVocê acertou {(acertos / len(perguntas) * 100):.0f}% das perguntas\n'


# Criando funções para manipular arquivos json.
def perguntas_json(local):
    """
    Esta função abre um arquivo json e retorna um dicionário com as perguntas e respostas.
    - local: Local do arquivo json.
    - return: Retorna um dicionário com as informações do arquivo.
    """
    import json  # Importando o módulo json.

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
    import json  # Importando o módulo json.
    
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



# Área de testes:
if __name__ == '__main__':  # Nenhum comando dentro deste bloco será executado se o arquivo atual for importado.
    import os  # Importando o módulo os.
    import json  # Importando o módulo json.
    
    caminho = os.path.dirname(os.path.realpath(__file__))  # Pegando o caminho do arquivo atual
    local =  f'{caminho}\pessoas.json'  # Local com o nome do arquivo.json

    # Programa para ler o arquivo.json e escrever ou criar um novo caso não exista.
    while True:
        try:
            print(f'\nDeseja:\n1 - Ler o arquivo.json\n2 - Escrever no arquivo.json\n3 - Sair')
            opção = int(input('Opção: '))

            if opção == 3:
                print(f'\nFinalizando...\n')
                break

            if opção < 1 or opção > 3:
                raise ValueError
        except:
            print('Opção inválida!')
            continue
        else:
            if opção == 1:
                dicionario = perguntas_json(local)  # Carregando o arquivo.json já convertido em dicionário.
                
                if not dicionario:  # Verificando se o dicionário está vazio.
                    print('\nNenhum dado encontrado!')
                    continue

                print()
                for key, value in dicionario.items():  # Imprimindo o dicionário
                    print(f'{key} = {value}')

            if opção == 2:
                while True:
                    try:
                        nome = str(input('\nNome: ')).title()  # Pegando o nome da pessoa.

                        idade = int(input('Idade: '))  # Pegando a idade da pessoa.

                        sexo = str(input('Sexo: [M/F] ')).upper()[0]  # Pegando o sexo da pessoa.
                    except Exception as e:
                        print(f'ERROR: {e}')
                        continue
                    else:
                        pessoa = f'Pessoa {len(perguntas_json(local)) + 1}'  # Criando um índice de pessoa nova para o arquivo.json
                        
                        dicionario = dict()  # Criando um dicionário vazio para armazenar as respostas.
                        
                        dicionario[pessoa] = {'Nome': nome, 'Idade': idade, 'Sexo': sexo}  # Adicionando a pessoa ao dicionário.

                        escrever_json(local, dicionario)  # Escrevendo os dados do dicionário no arquivo.json
                        
                        print(f'\n"{pessoa}" Adicionada ao arquivo.json com sucesso!')

                        opção = input('\nDeseja continuar? [S/N] ')
                        if opção.upper()[0] in 'SN':
                            if opção.upper()[0] == 'N':
                                break

