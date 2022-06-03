from ex115.lib.interface import * # Utilizando o * para importar todos os módulos da biblioteca.
from ex115.lib.arquivo import * # Importando o módulo "arquivo" que verifica se o arquivo existe ou cria um.
from time import sleep # Importando o módulo sleep da biblioteca time.

print('===== EXERCÍCIO #115 =====')
print()

nome = 'Arquivo de Dados.txt' # Adicionando o nome do arquivo a variável.
arq = f".\CursoEmVideo\Exercicios\ex115\lib\{nome}" # Adicionando o caminho do arquivo a variável.

if not arquivoExiste(arq): # Verificando se o arquivo não existe.
    criarArquivo(arq) # Criando o arquivo.


while True:
# Criando um menu através da função menu() e retornando o valor da opção escolhida pelo usuário.
    opcao = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoa', 'Sair do Sistema'])

# Verificando a opção escolhida e chamando a função respectiva.
    if opcao == 1:
        lerArquivo(arq) # Chamando a função lerArquivo() para exibir o conteúdo do arquivo.
    elif opcao == 2:
        msg('OPÇÃO 2')
    elif opcao == 3:
        msg('Saindo do sistema... Até logo!')
        break
    sleep(2)
