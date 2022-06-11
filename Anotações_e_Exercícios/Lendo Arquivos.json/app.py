"""
Este programa verifica se o usuário quer ver o arquivo.json ou escrever novos dados nele, através das funções de leitura e escrita do módulo arquivo.py
"""
from arquivo import escrever_json, perguntas_json  # Importando as funções que estão no arquivo arquivo.py 
import os  # Importando o módulo os.

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
