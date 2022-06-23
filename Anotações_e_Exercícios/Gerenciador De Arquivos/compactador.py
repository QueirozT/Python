"""
Programa que localiza arquivos e permite compactar e descompactar.

Este programa utiliza o módulo "localizador" para acessar os arquivos do sistema através do local e parte do nome, e exibe a descrição deles. depois coleta os resultados e através deles permite compactar e descompactar em arquivos.zip

Módulos Importados:
    os: Módulo que permite acessar os arquivos do sistema.
        
        Funções:
            os.walk(caminho): Permite percorrer os diretórios do sistema. (USADO NO MÓDULO LOCALIZADOR.)
                Retorna: (caminho, lista de subdiretórios, lista de arquivos)
            
            os.path.splitext(caminho): Permite separar o nome do arquivo e a extensão. (USADO NO MÓDULO LOCALIZADOR.)
                Retorna: (caminho, extensão)
            
            os.path.getsize(caminho): Obtem o tamanho do arquivo. (USADO NO MÓDULO LOCALIZADOR.)
                Retorna: Tamanho do arquivo em bytes.

            os.path.exists(caminho): Verificar se o caminho existe. (USADO NO MÓDULO GERENCIADOR)
                Retorna: True se o caminho existe, False se não existe.

            os.path.isfile(caminho_completo): Verifica se existe e é um arquivo.
                Retorna: True, se o arquivo existe, False se não existe ou não é um arquivo.
            
            os.path.join(caminho, nome_arquivo): Permite juntar um caminho e um nome de arquivo.
                Retorna: caminho + nome_arquivo
    
    uteis: Módulo que contém funções úteis para o programa.

        Funções:
            converte(tamanho): Função que converte de bytes para M, G, etc. (USADO NO MÓDULO LOCALIZADOR.)
                Retorna: Tamanho do arquivo convertido em K, M, G, etc.
            
            cor(num): Função que retorna uma cor
                Retorna: Cor do número especificado.

    localizador: Módulo que contém as funções do programa de localização de arquivos.

        Funções:
            localizar(caminho): Função que localiza arquivos através do caminho e parte do nome.
                Retorna: Lista de caminhos dos arquivos encontrados.
"""
from localizador import localizador
from gerenciador import verificar
from uteis import cor
from zipfile import ZipFile
import os
 

def compactar(local: str, nome: str, lista: list) -> str:
    """
    Função que compacta multiplos arquivos em um arquivo.zip

    Esta função recebe um local, um nome para o novo arquivo.zip e uma lista com os caminhos dos arquivos que serão compactados.

        Parâmetros:
            local (str): Local onde será armazenado o arquivo.zip
            nome (str): Nome do novo arquivo.zip
            lista (list): Uma lista com os caminhos dos arquivos que serão compactados

        Retorno:
            print(): Mostra uma mensagem de sucesso ou de erro
    """
    local = os.path.join(local, f'{nome}.zip')
    try:
        with ZipFile(local, 'w') as zip:
            for caminho, arquivo in lista:
                caminho_completo = os.path.join(caminho, arquivo)
                zip.write(caminho_completo, arquivo)
        print(f'\n{cor(2)}O arquivo "{cor(3)}{nome}" {cor(2)}foi compactado com sucesso!{cor(0)}\n')
    except Exception as e:
        print(f'\n{cor(1)}Erro ao compactar:{cor(4)} {e}{cor(0)}\n')


def descompactar(caminho_arquivo: str, caminho_novo: str) -> str:
    """
    Função que descompacta um arquivo.zip

    Esta função recebe o caminho do arquivo compactado e o novo caminho para descompactar e criar uma pasta com os arquivos.

        Parâmetros:
            caminho_arquivo (str): Caminho do arquivo.zip
            caminho_novo (str): Caminho para o novo arquivo descompactado

        Retorno:
            print(): Mostra uma mensagem de sucesso ou de erro.
    """
    try:
        with ZipFile(caminho_arquivo, 'r') as zip:
            zip.extractall(caminho_novo)
        print(f'\n{cor(2)}O arquivo "{cor(3)}{caminho_novo}" {cor(2)}foi descompactado com sucesso!{cor(0)}\n')
    except Exception as e:
        print(f'\n{cor(1)}Erro ao descompactar:{cor(4)} {e}{cor(0)}\n')


def arquivos_zipados(caminho_completo: str) -> str:
    """
    Função que mostra os arquivos compactados

    Esta função recebe um caminho para um arquivo compactado e lista todos os arquivos dentro dele.

        Parâmetros:
            caminho_completo (str): Caminho do arquivo.zip

        Retorno:
            print(): Exibe uma mensagem de sucesso ou de erro.
    """
    try:
        if not os.path.isfile(caminho_completo):
            raise FileNotFoundError

        with ZipFile(caminho_completo, 'r') as zip:
            print(f'\n{cor(2)}Os arquivos zipados são:{cor(0)}')
            for arquivo in zip.namelist():
                print(f'\t{cor(4)}{arquivo}') # Mostrando o nome de todos os arquivos zipados.
    except Exception as e:
        print(f'\n{cor(1)}Erro ao exibir os arquivos:{cor(4)} {e}{cor(0)}\n')



# Programa Principal / Área de Testes
if __name__ == '__main__':
    print(f'\n{cor(4)}{"":=^50}\n{cor(3)}{"PROGRAMA COMPACTADOR DE ARQUIVOS":^50}\n{cor(4)}{"":=^50}{cor(0)}')

    while True:
        opcao = input(f'\n{cor(3)}Deseja Compactar ou Descompactar? {cor(4)}[ZIP/UNZIP] {cor(2)}').upper()
        if not opcao in "UNZIP":
            print(f'{cor(1)}Opção Inválida!{cor(0)}')
            continue

        # Compactar
        if opcao == 'ZIP':
            print(f'\n{cor(4)}{"":=^30}\n{cor(3)}{"COMPACTADOR":^30}\n{cor(4)}{"":=^30}{cor(0)}')
            arquivos = list()

            while True:
                caminho = verificar(f'\n{cor(3)}Qual o caminho? {cor(2)}')
                nome = input(f'\n{cor(3)}Qual o nome do arquivo? {cor(2)}')

                arquivo = localizador(caminho, nome)

                if len(arquivo) > 1:
                    while True:
                        if len(arquivo) > 2:
                            opcao = input(f'{cor(3)}Deseja adicionar todos os arquivos encontrados ao arquivo.zip? {cor(4)}[S/N] {cor(2)}').upper()[0]
                            if not opcao in "SN":
                                print(f'{cor(1)}Opção Inválida!{cor(0)}')
                                continue
                            if opcao == 'S':
                                for i in range(1, len(arquivo)):
                                    arquivos.append([arquivo[i][0], arquivo[i][1]])
                                break
                        
                        while True:
                            opcao = input(f'\n{cor(3)}Deseja adicionar um dos arquivos encontrados ao arquivo.zip? {cor(4)}[S/N] {cor(2)}').upper()[0]
                            if not opcao in 'SN':
                                print(f'{cor(1)}Opção Inválida!{cor(0)}')
                                continue
                            if opcao == 'S':
                                while True:
                                    try:
                                        num = int(input(f'\n{cor(3)}Qual o N° do arquivo? {cor(2)}'))
                                        if num > (len(arquivo) - 1) or num < 1:
                                            raise ValueError
                                    except:
                                        print(f'{cor(1)}Opção Inválida!{cor(0)}')
                                    else:
                                        arquivos.append([arquivo[num][0], arquivo[num][1]])
                                        break
                            break
                        break

                while True:
                    opcao = input(f'\n{cor(3)}Deseja adicionar outros arquivos? {cor(4)}[S/N] {cor(2)}').upper()[0]
                    if opcao in 'SN':
                        break
                    print(f'{cor(1)}Opção Inválida!{cor(0)}')
                if opcao == 'S':
                    continue
                
                local = verificar(f'\n{cor(3)}Onde deseja salvar seu arquivo.zip? {cor(2)}')
                nome = input(f'{cor(3)}Qual vai ser o nome do arquivo.zip? {cor(2)}')

                compactar(local, nome, arquivos)  # Criando o arquivo.zip
                break
            break
            
        # Descompactar
        if opcao == 'UNZIP':
            print(f'\n{cor(4)}{"":=^30}\n{cor(3)}{"DESCOMPACTADOR":^30}\n{cor(4)}{"":=^30}{cor(0)}')

            while True:
                caminho = verificar(f'\n{cor(3)}Qual o caminho? {cor(2)}')
                nome = input(f'\n{cor(3)}Qual o nome do arquivo.zip? {cor(2)}')

                arquivo = localizador(caminho, nome)

                if len(arquivo) > 1 and ".zip" in "".join([x + y for x, y in arquivo]):
                    while True:
                        try:
                            num = int(input(f'{cor(3)}Qual o N° do arquivo.zip? {cor(2)}'))
                            if num > (len(arquivo) - 1) or num < 1:
                                raise ValueError
                        except:
                            print(f'{cor(1)}Opção Inválida!{cor(0)}')
                        else:
                            caminho_arquivo = os.path.join(arquivo[num][0], arquivo[num][1])
                            caminho_novo = caminho_arquivo.replace('.zip', '')

                            descompactar(caminho_arquivo, caminho_novo)  # Descompactando o arquivo.zip
                            break
                else:
                    print(f'{cor(1)}Nenhum arquivo.zip encontrado!{cor(0)}')
                    continue
                break
            break
    print(f'{cor(1)}Finalizando...{cor(0)}\n')
