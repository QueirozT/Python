"""
Este módulo contém funções que simulam um banco de dados.

Este módulo contém funções de leitura e escrita e foi criado no intúito de simulam um banco de dados de forma extremamente simples.
"""

import os
import json
from typing import Union  # Importando o Union para mesclar o type hint das funções (Entrada e Saída de dados esperada).

local = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Contas.json'))


def write(valor: dict, literal: bool=False) -> None:
    """
    Função de escrita.

    Esta função simula a escrida de um banco de dados, armazenando valores em um arquivo.json. ela recebe dois parâmetros, os dados em formato de dicionário e um parâmetro opcional que caso verdadeiro permite sobrescrever todos os dados do banco de dados pelos valores informados.

        Parametros:
            valor (dict):
                Dados a serem escritos.
            literal (bool) - Opcional:
                True - Escreve exatamente os dados que receber, sobrescrevendo os valores do banco de dados. 
                False (Padrão) - Adiciona os novos valores, atualizando o banco de dados.

        Retorno:
            None
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


def read() -> dict:
    """
    Função de leitura

    Esta função simula a leitura de um banco de dados. ela abre o arquivo.json, coleta os valores, converte em um dicionário e retorno o dicionário com os valores.

        Retorno:
            arquivo (dict): Um dicionário com todos os valores do banco de dados.
    """
    arquivo = dict()
    try:
        with open(local, 'r') as f:
            arquivo = json.load(f)
    except:
        with open(local, 'w+'):
            pass

    return arquivo


def atualizar(agencia: str, conta: str, saldo: float, limite: int=0) -> None:
    """
    Esta função atualiza o banco de dados.

    Esta função recebe os dados de uma conta, valida o tipo de conta a quem os dados pertencem. abre o banco de dados colentando um dicionário, adiciona os valores da conta ao dicionário e depois escreve os valores novos no banco de dados.

        Parametros:
            agencia (str):
                Chave da agência da conta.
            conta (str):
                Chave do número da conta.
            saldo (int, float): 
                Valor do saldo da conta.
            limite (int) - Opcional:
                Valor do limite da conta (Apenas para Conta-Corrente).
        
        Retorno:
            None: Os dados serão validados e adicionados ao banco de dados no momento em que a função for chamada.
    """
    if limite:  # Valida o tipo de conta a quem os dados pertencem
        dados = {agencia: {conta: {"agencia": agencia, "conta": conta, "saldo": saldo, "ContaCorrente": {"limite": limite}}}}
    else:
        dados = {agencia: {conta: {"agencia": agencia, "conta": conta, "saldo": saldo, "ContaPoupanca": {"limite": limite}}}}
    
    bd = read()  # Carrega um dicionário com os dados do banco de dados

    if bd.get(agencia):  # Atualiza o dicionário com os novos dados
        bd[agencia][conta] = dados[agencia][conta]
    else:
        bd.update(dados)

    write(bd)  # Salva os novos dados no banco de dados
    

def remover(agencia: str, conta: str) -> None:
    """
    Esta função remove dados específicos do banco de dados.

    Esta função recebe duas chaves como parâmetro, uma delas opcional. Verifica se as chaves informados estão no banco de dados e apaga os respectivos dados. depois atualiza o banco de dados com o parâmetro "literal=True" que sobrescreve o banco de dados com os novos valores e exibe uma mensagem. caso as chaves não sejam encontradas, retorna outra mensagem.

        Parametros:
            agencia (str): 
                Chave da agência da conta.
            conta (str) - Opcional:
                Chave do número da conta.
        
        Retorno:
            None: Exibe uma mensagem de erro ou de sucesso.
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


def buscar(agencia: str, conta: str=None) -> Union(dict, None):
    """
    Esta função busca as chaves no banco de dados e retorna os valores.

    Esta função recebe duas chaves como parâmetro, uma opcional. Verifica se as chaves informadas estão no banco de dados e retorna os dados das respectivas chaves. caso não as encontre, retorna None.

        Parametros:
            agencia (str):
                chave da agência da conta
            conta (str, None) - Opcional:
                Chave do número da conta.
                Caso não informado, irá retornar todos os valores da chave da agência.

        Retorno:
            dict or None: Caso ambas as chaves sejam informadas, retorna um dicionário com os dados da conta. Caso a conta não seja informada, retorna todas as contas da chave agência. E caso os dados não sejam encontrados, retorna None.
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


def listar() -> None:
    """
    Esta função lista todas as chaves do banco de dados.

    Esta função coleta o dicionário com os dados do banco de dados e exibe apenas as chaves agência e conta armazenadas. Caso não existam dados armazenados, exibe uma mensagem.

        Retorno:
            None: Exibe uma mensagem caso não existam dados ou exibe as chaves organizadas por agência -> contas.
    """
    dados = read()
    if dados == {}:
        print('Não há contas no banco de dados.')    
    else:
        for a, c in dados.items():
            print(f'Agência: {a}')
            for c, d in c.items():
                print(f'\tConta: {c}')
