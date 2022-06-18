import os
import json

local = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Contas.json'))


def write(valor, literal=False):
    """
    Esta função escreve ou atualiza os dados do banco de dados em um arquivo.json
    - valor: Dados a serem escritos.
    - literal: (Opcional) Se True, escreve exatamente os dados que receber. se False, só adiciona os novos valores.
    """
    arquivo = dict()
    try:
        with open(local, 'r') as f:
            arquivo = json.load(f)
    except:
        with open(local, 'w+') as f:
            pass
    finally:
        with open(local, 'w') as f:
            if literal:
                f.write(json.dumps(valor, indent=True))
                return
            arquivo.update(valor)
            f.write(json.dumps(arquivo, indent=True))


def read():
    """
    Esta função lê o arquivo.json do banco de dados e retorna um dicionário.
    """
    arquivo = dict()
    try:
        with open(local, 'r') as f:
            arquivo = json.load(f)
    except:
        with open(local, 'w+'):
            pass

    return arquivo


def atualizar(agencia, conta, saldo, limite=0):
    """
    Esta função Atualiza ou adiciona os dados de uma conta ao banco de dados.
    - agencia: Chave da agência da conta.
    - conta: Chave do número da conta.
    - saldo: Valor do saldo da conta.
    - limite: (Conta-Corrente) Valor do limite da conta.
    """
    if limite:
        dados = {agencia: {conta: {"agencia": agencia, "conta": conta, "saldo": saldo, "ContaCorrente": {"limite": limite}}}}
    else:
        dados = {agencia: {conta: {"agencia": agencia, "conta": conta, "saldo": saldo, "ContaPoupanca": {"limite": limite}}}}
    
    bd = read()  # Carrega os dados do banco de dados

    if bd.get(agencia):
        bd[agencia][conta] = dados[agencia][conta]
    else:
        bd.update(dados)

    write(bd)  # Salva os novos dados no banco de dados
    

def remover(agencia, conta):
    """
    Esta função Remove os dados de uma conta do banco de dados.
    - agencia: Chave da agência da conta.
    - conta: Chave do número da conta.
    """
    dados = read()
    try:
        dados[agencia].pop(conta)
        if dados[agencia] == {}:
            dados.pop(agencia)
    except:
        print('NÃO ENCONTRADO')
    else:
        print('APAGADO!')
        write(dados, literal=True)


def buscar(agencia, conta=None):
    """
    Esta função Busca os dados de uma conta no banco de dados.
    Se a conta não for especificada, mostra todas as contas da agência.
    - agencia: Chave da agência da conta.
    - conta: Chave do número da conta.
    """
    try:
        if conta == None:
            dados = read()
            return dados[agencia]
        else:
            dados = read()
            return dados[agencia][conta]
    except:
        return None


def listar():
    """
    Mostra todas as contas do banco de dados.
    Caso não existam contas, mostra uma mensagem.
    """
    dados = read()
    if dados == {}:
        print('Não há contas no banco de dados.')    
    else:
        for a, c in dados.items():
            print(f'Agência: {a}')
            for c, d in c.items():
                print(f'\tConta: {c}')
