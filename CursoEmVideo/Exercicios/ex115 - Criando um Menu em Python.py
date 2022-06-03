from ex115.lib.interface import * # Utilizando o * para importar todas as funções da biblioteca.
from time import sleep # Importando o módulo sleep da biblioteca time.

print('===== EXERCÍCIO #115 =====')
print()

while True:
# Criando um menu através da função menu() e retornando o valor da opção escolhida pelo usuário.
    opcao = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoa', 'Sair do Sistema'])

# Verificando a opção escolhida e chamando a função respectiva.
    if opcao == 1:
        msg('OPÇÃO 1')
    elif opcao == 2:
        msg('OPÇÃO 2')
    elif opcao == 3:
        msg('Saindo do sistema... Até logo!')
        break
    sleep(2)
