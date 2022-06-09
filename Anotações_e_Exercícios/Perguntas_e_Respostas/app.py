"""
Este programa apresenta uma série de perguntas ao usuário e registra as respostas, ao final mostra a porcentagem de acertos.
"""
from regras import *  # Importando as funções que estão no arquivo regras para executar o programa.

print('Bem vindo ao programa de perguntas e respostas!\n')

local = f'.\Anotações_e_Exercícios\Perguntas_e_Respostas\perguntas.txt'  # Definindo o caminho para o arquivo com as perguntas.

lista = perguntas(local)  # Executando a função perguntas() e passando o parâmetro local para coletar as perguntas.

acertos = 0

for key, value in lista.items():
    print(f'{key}: {value["pergunta"]}')  # Mostrando a pergunta
    
    for item in value["respostas"]:  # Iterando a lista dentro de "respostas"
        for respKey, respValue in item.items():  # Desenpacotando os dicionários
            print(f'[{respKey}] = {respValue}')  # Mostrando as alternativas e as respostas.
    
    acertos += 1 if resposta(value) else 0  # Coletando e verificando se a resposta está correta com a função resposta()
    print()

print(porcentagemAcerto(acertos, lista))  # Mostrando a estimativa de acertos com a função porcentagemAcerto()
