"""
Programa simples para fazer Web Scraping

Este programa utiliza as biblioteclas externas "requests" e "beautifulsoup4" para fazer uma requisição que retorna o html de uma página e analiza o html recebido coletando as informações desejadas através dos identificadores css.

Módulos Importados:

    requests: É uma biblioteca que permite enviar solicitações HTTP pelo python, permitindo a utilização de APIs no Python.

        Funções:
            requests.get(url): Envia uma requisição para o url informado.
                Retorno: Retorna o status <Response [200]>, e permite coletar o html através do parâmetro .text


    bs4 "beautifulsoup4": Beautiful Soup é uma biblioteca Python de extração de dados de arquivos HTML e XML.
        
        Funções:
            BeautifulSoup(valor, 'formato.iterpretador'): Método que recebe um html e aplica seu próprio interpretador (parser).
                Retorna: Um item da class BeautifulSoup que permite manipular facilmente o html.

                Sub-Funções:
                    .select(seletor css): Coleta todos os itens do html com o #id ou .class especificados.
                        Return: Uma lista com todos os itens.
                    
                    .select_one(seletor css): Coleta o primeiro item do html com o #id ou .class especificado
                        Return: Um item de classe.

                    .text: Permite coletar apenas o texto de um item html
                        Return: Um item de classe que pode ser convertido Ex: através de ListComprehensions.
"""
import requests
from bs4 import BeautifulSoup
 
# Passando o url do site que terá os dados coletados.
url = 'https://pt.stackoverflow.com/questions/tagged/python'
 
# Fazendo a requisição com o requests e recebendo a resposta
response = requests.get(url)
if not response:
    print(f'\n\033[34m\nURL: \033[36m{url}\n\033[34mRESPOSTA: \033[31m{response} = Response Failed!\n\033[m')
else:
    print(f'\n\033[34m\nURL: \033[36m{url}\n\033[34mRESPOSTA: \033[32m{response} = Response OK!\n\033[m')

    # Utilizando o BeautifulSoup para analizar o html recebido pelo response.text
    html = BeautifulSoup(response.text, 'html.parser')

    # Coletando as perguntas do site através do método .select(seletor css) que retorna uma lista
    for pergunta in html.select('.s-post-summary'):

        # Coletando os títulos as datas e os votos através do select_one(seletor css) que retorna apenas o primeiro item que encontrar.
        titulo = pergunta.select_one('.s-post-summary--content-title')
        titulo = ''.join([t for t in titulo.text]).replace('\n', ' ')
        
        # O BeautifulSoup tem um método que coletam apenas o valor sem pegar o html que é o ".text"
        data = pergunta.select_one('.relativetime')
        data = ''.join([d for d in data.text]).replace('\n', ' ')

        votos = pergunta.select_one('.s-post-summary--stats-item')
        # Estou usando List Comprehensions para iterar sobre os valores e remover as quebras de linha.
        votos = ''.join([v for v in votos.text]).replace('\n', ' ')

        # Exibindo os valores coletados de cada pergunta formatados e convertidos para str pelo list comprehensions
        print(f'\033[34mTempo Relativo: \033[36m{data}\t \033[34mVotos: \033[36m{votos}\n\033[34mTítulo: \033[32m{titulo}\n\033[m')
