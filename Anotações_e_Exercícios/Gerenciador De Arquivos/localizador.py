"""
Programa que localiza e exibe a descrição de um arquivo.

Este programa recebe um caminho e um nome de arquivo ou parte dele e tenta localizar o arquivo no caminho especificado. retornando uma série de informações do arquivo encontrado.

Módulos Importados:
    os: Módulo que permite acessar os arquivos do sistema.
        
        Funções:
            os.walk(caminho): Permite percorrer os diretórios do sistema.
                Retorna: (caminho, lista de subdiretórios, lista de arquivos)
            
            os.path.join(caminho, nome_arquivo): Permite juntar um caminho e um nome de arquivo.
                Retorna: caminho + nome_arquivo
            
            os.path.splitext(caminho): Permite separar o nome do arquivo e a extensão.
                Retorna: (caminho, extensão)
            
            os.path.getsize(caminho): Permite obter o tamanho do arquivo.
                Retorna: Tamanho do arquivo em bytes.
    
    uteis: Módulo que contém funções úteis para o programa.
        converte(tamanho): Função que converte de bytes para M, G, etc.
            Retorna: Tamanho do arquivo convertido em K, M, G, etc.
        
        cor(num): Função que retorna uma cor
            Retorna: Cor do número especificado.
"""
from uteis import converte, cor
import os


def localizador(caminho_procura, arquivo_procura):
    cont = 0
    itens = [['Caminhos', 'Arquivo'],]
    for raiz, diretorios, arquivos in os.walk(caminho_procura):  # descompactando o gerador os.walk()
        for arquivo in arquivos:  # percorrendo os arquivos
            if arquivo_procura in arquivo or not arquivo_procura:  # verificando se o arquivo procurado está nos arquivos ou não foi informado.
                try:
                    cont += 1
                    caminho_completo = os.path.join(raiz, arquivo)  # Função que junta o caminho com o nome do arquivo
                    nome_arquivo, ext_arquivo = os.path.splitext(arquivo)  # Função que separa o nome do arquivo e a extensão
                    tamanho = os.path.getsize(caminho_completo)  # Função que retorna o tamanho do arquivo em bytes

                    itens.append([raiz, arquivo])  # Salvando o caminho de cada arquivo encontrado

                    print(f'\n{cor(4)}{cont}° Arquivo encontrado: {cor(2)}{arquivo}{cor(0)}')
                    print(f'{cor(4)}Caminho: {cor(2)}{caminho_completo}{cor(0)}')
                    print(f'{cor(4)}Nome: {cor(2)}{nome_arquivo}{cor(0)}')
                    print(f'{cor(4)}Extensão: {cor(2)}{ext_arquivo}{cor(0)}')
                    print(f'{cor(4)}Tamanho: {cor(2)}{converte(tamanho)}{cor(0)}')
                except PermissionError:
                    print(f'{cor(1)}Sem permissões!{cor(0)}')
                except FileNotFoundError:
                    print(f'{cor(1)}Arquivo não encontrado!{cor(0)}')
                except Exception as e:
                    print(f'{cor(1)}Erro desconhecido: {e}{cor(0)}')

    print(f'\n{cor(2)}{cont} arquivo(s) encontrado(s).{cor(0)}\n')
    return itens


# Programa Principal / Área de Testes
if __name__ == '__main__':
    print(f'\n{cor(4)}{"=" * 40}\n{cor(3)}{"LOCALIZADOR DE ARQUIVOS":^40}\n{cor(4)}{"=" * 40}\n{cor(0)}')

    caminho_procura = input(f'{cor(3)}Informe o caminho: {cor(2)}')
    arquivo_procura = input(f'\n{cor(3)}Informe o nome do arquivo: {cor(2)}')

    resultado = localizador(caminho_procura, arquivo_procura)  # Chamando a função localizador

    print(resultado)  # Exibindo o resultado da função localizador (Lista com diretório dos arquivos encontrados)

    localizador(resultado[1][0], resultado[1][1])  # Chamando a função localizador com o caminho e o nome do primeiro arquivo
