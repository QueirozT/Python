from ex115.lib.interface import * # Utilizando o * para importar todos os módulos da biblioteca.
from ex115.lib.arquivo import * # Importando o módulo "arquivo" que verifica se o arquivo existe ou cria um.
from time import sleep # Importando o módulo sleep da biblioteca time.

print('===== EXERCÍCIO #115 =====')
print()

nome = 'Arquivo de Dados.txt' # Adicionando o nome do arquivo a variável.
local = f".\CursoEmVideo\Exercicios\ex115\lib\{nome}" # Adicionando o caminho do arquivo a variável.

if not arquivoExiste(local): # Verificando se o arquivo não existe.
    criarArquivo(nome, local) # Criando o arquivo.


while True:
# Criando um menu através da função menu() e retornando o valor da opção escolhida pelo usuário.
    opcao = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoa', 'Sair do Sistema'])

# Verificando a opção escolhida e chamando a função respectiva.
    if opcao == 1:
        lerArquivo(local) # Chamando a função lerArquivo() para exibir o conteúdo do arquivo.
    elif opcao == 2:
        msg('NOVO CADASTRO')
        nome = str(input(f'{cor(4)}Nome: {cor(3)}')).strip().title() # Recebendo um Nome
        idade = lerInt('Idade: ') # Recebendo uma Idade
        cadastrar(local, nome, idade) # Chamando a função cadastrar() para adicionar o nome e idade ao arquivo.
    elif opcao == 3 or opcao == 0:
        msg('Saindo do sistema... Até logo!')
        break
    sleep(2)
