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
