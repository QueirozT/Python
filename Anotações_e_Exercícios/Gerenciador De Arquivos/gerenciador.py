"""
Programa que localiza e exibe a descrição de um arquivo e permite manipula-lo.

Este programa é a versão 2.0 do programa "localizador de arquivos". ele utiliza o programa anterior como base para acessar os arquivos e exibir a descrição deles, depois coleta os resultados e através deles manipula os arquivos encontrados.

Módulos Importados:
    os: Módulo que permite acessar os arquivos do sistema.
        
        Funções:
            os.walk(caminho): Permite percorrer os diretórios do sistema. (USADO APENAS NO LOCALIZADOR.)
                Retorna: (caminho, lista de subdiretórios, lista de arquivos)
            
            os.path.join(caminho, nome_arquivo): Permite juntar um caminho e um nome de arquivo.
                Retorna: caminho + nome_arquivo
            
            os.path.splitext(caminho): Permite separar o nome do arquivo e a extensão. (USADO APENAS NO LOCALIZADOR.)
                Retorna: (caminho, extensão)
            
            os.path.getsize(caminho): Permite obter o tamanho do arquivo. (USADO APENAS NO LOCALIZADOR.)
                Retorna: Tamanho do arquivo em bytes.

            os.path.exists(caminho): Permite verificar se o caminho existe.
                Retorna: True se o caminho existe, False se não existe.
    
    shutil: Módulo que permite manipular arquivos.

        Funções:
            shutil.copy(caminho_origem, caminho_destino): Permite copiar um arquivo.
                Retorna: None

            shutil.move(caminho_origem, caminho_destino): Permite mover um arquivo.
                Retorna: None

            shutil.remove(caminho_completo): Permite remover um arquivo.
                Retorna: None
    
    uteis: Módulo que contém funções úteis para o programa.
        converte(tamanho): Função que converte de bytes para M, G, etc. (USADO APENAS NO LOCALIZADOR.)
            Retorna: Tamanho do arquivo convertido em K, M, G, etc.
        
        cor(num): Função que retorna uma cor
            Retorna: Cor do número especificado.

    localizador: Módulo que contém as funções do programa de localização de arquivos.
        localizar(caminho): Função que localiza os arquivos do sistema.
            Retorna: Lista de caminhos dos arquivos encontrados.
"""
from localizador import localizador
from uteis import cor
import shutil
import os


def copiar(caminho_origem, caminho_destino):
    """
    Função que copia um arquivo.

    Esta função recebe um caminho de origem que contém o nome do arquivo e um caminho de destino e copia o arquivo de origem para o destino.

        Parâmetros:
            caminho_origem: Caminho do arquivo de origem.
            caminho_destino: Caminho de destino do arquivo.

        Retorno:
            print(): retorna uma mensagem de sucesso. Caso ocorra algum erro, retorna a mensagem de erro.
    """
    try:
        shutil.copy(caminho_origem, caminho_destino)
        print(f'{cor(2)}Arquivo copiado com sucesso!{cor(0)}')
    except PermissionError:
        print(f'{cor(1)}Sem permissões!{cor(0)}')
    except FileNotFoundError:
        print(f'{cor(1)}Arquivo não encontrado!{cor(0)}')
    except Exception as e:
        print(f'{cor(1)}Erro desconhecido: {e}{cor(0)}')


def mover(caminho_origem, caminho_destino):
    """
    Função que move um arquivo.

    Esta função recebe um caminho de origem que contém o nome do arquivo e um caminho de destino e move o arquivo de origem para o destino.

        Parâmetros:
            caminho_origem: Caminho do arquivo de origem.
            caminho_destino: Caminho de destino do arquivo.

        Retorno:
            print(): retorna uma mensagem de sucesso. Caso ocorra algum erro, retorna a mensagem de erro.
    """
    try:
        shutil.move(caminho_origem, caminho_destino)
        print(f'{cor(2)}Arquivo movido com sucesso!{cor(0)}')
    except PermissionError:
        print(f'{cor(1)}Sem permissões!{cor(0)}')
    except FileNotFoundError:
        print(f'{cor(1)}Arquivo não encontrado!{cor(0)}')
    except Exception as e:
        print(f'{cor(1)}Erro desconhecido: {e}{cor(0)}')


def remover(caminho_completo):
    """
    Função que remove um arquivo.

    Esta função recebe o caminho completo do arquivo e remove ele do sistema.

        Parâmetros:
            caminho_completo: Caminho completo do arquivo.

        Retorno:
            print(): retorna uma mensagem de sucesso. Caso ocorra algum erro, retorna a mensagem de erro.
    """
    try:
        os.remove(caminho_completo)
        print(f'{cor(2)}Arquivo excluído com sucesso!{cor(0)}')
    except PermissionError:
        print(f'{cor(1)}Sem permissões!{cor(0)}')
    except FileNotFoundError:
        print(f'{cor(1)}Arquivo não encontrado!{cor(0)}')
    except Exception as e:
        print(f'{cor(1)}Erro desconhecido: {e}{cor(0)}')


def verificar(msg):
    """
    Função que verifica se o caminho informado existe.

    Esta função recebe uma mensagem que é exibida ao usuário enquanto coleta um caminho e verifica se o caminho informado existe.

        Parâmetros:
            msg: Mensagem que é exibida ao usuário.

        Retorno:
            caminho: Caminho do arquivo.
    """
    while True:
        caminho_destino = input(msg)
        if os.path.exists(caminho_destino):
            return caminho_destino
        print(f'{cor(1)}Caminho não encontrado!{cor(0)}')



# Programa Principal / Área de Teste
if __name__ == '__main__':
    print(f'\n{cor(4)}{"=" * 40}\n{cor(3)}{"GERENCIADOR DE ARQUIVOS":^40}\n{cor(4)}{"=" * 40}{cor(0)}')
    
    while True:
        # Coletando o caminho e o nome do arquivo que será procurado
        caminho_procura = verificar(f'\n{cor(3)}Informe o caminho: {cor(2)}')
        arquivo_procura = input(f'\n{cor(3)}Informe o nome do arquivo: {cor(2)}')
        
        # Salvando todos os arquivos encontrados
        arquivos = localizador(caminho_procura, arquivo_procura)
        
        # Verificando se deseja procurar novamente ou manipular os arquivos encontrados
        while True:
            opcao = input(f'{cor(3)}Procurar novamente? {cor(4)}[S/N] {cor(2)}')
            opcao = opcao[0] if opcao else '...'
            if opcao.upper() in 'SN':
                break
            print(f'{cor(1)}Opção inválida!{cor(0)}')

        if opcao.upper() == 'S':
            continue
        if opcao.upper() == 'N':
            if len(arquivos) == 1:  # Verificando se existem arquivos encontrados.
                break
            
            while True:
                opcao = input(f'\n{cor(3)}Deseja copiar, mover ou remover? {cor(4)}[C/M/R] {cor(3)}ou {cor(1)}[F] {cor(3)}para finalizar: {cor(2)}')
                opcao = opcao[0] if opcao else ''

                # Finalizar o programa
                if opcao.upper() == 'F':
                    break

                # Copiar o arquivo
                if opcao.upper() == 'C':
                    while True:
                        try:
                            item = input(f'\n{cor(3)}Qual arquivo deseja Copiar? [N°]{cor(2)} ')
                            item = int(item[0]) if item else 0
                            if item > (len(arquivos) - 1) or item == 0:
                                raise ValueError
                        except ValueError:
                            print(f'{cor(1)}Valor inválido!{cor(0)}')
                            continue
                        else:
                            caminho_origem = os.path.join(arquivos[item][0], arquivos[item][1])
                            caminho_destino = verificar(f'{cor(3)}Informe o caminho de destino: {cor(2)}')

                            copiar(caminho_origem, caminho_destino)
                            break
                    break

                # Mover o arquivo
                if opcao.upper() == 'M':
                    while True:
                        try:
                            item = input(f'\n{cor(3)}Qual arquivo deseja Mover? [N°]{cor(2)} ')
                            item = int(item[0]) if item else 0
                            if item > (len(arquivos) - 1) or item == 0:
                                raise ValueError
                        except ValueError:
                            print(f'{cor(1)}Valor inválido!{cor(0)}')
                            continue
                        else: 
                            caminho_origem = os.path.join(arquivos[item][0], arquivos[item][1])
                            caminho_destino = verificar(f'{cor(3)}Informe o caminho de destino: {cor(2)}')
                            
                            mover(caminho_origem, caminho_destino)
                            break
                    break

                # Remover o arquivo
                if opcao.upper() == 'R':
                    while True:
                        try:
                            item = input(f'\n{cor(3)}Qual arquivo deseja Remover? [N°]{cor(2)} ')
                            item = int(item[0]) if item else 0
                            if item > (len(arquivos) - 1) or item == 0:
                                raise ValueError
                        except ValueError:
                            print(f'{cor(1)}Valor inválido!{cor(0)}')
                            continue
                        else: 
                            caminho_completo = os.path.join(arquivos[item][0], arquivos[item][1])

                            opcao = input(f'{cor(1)}Tem certeza que deseja Remover o arquivo {arquivos[item][1]}? {cor(4)}[S/N] {cor(2)}')
                            opcao = opcao[0] if opcao else ''

                            if opcao.upper() == 'S':
                                remover(caminho_completo)
                                break
                            if opcao.upper() == 'N':
                                break
                            print(f'{cor(1)}Opção inválida!{cor(0)}')
                    break
                print(f'{cor(1)}Opção inválida!{cor(0)}')
            break
    print(f'{cor(1)}Finalizando...{cor(0)}\n')
