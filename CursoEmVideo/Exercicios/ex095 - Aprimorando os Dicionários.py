print('===== EXERCÍCIO #095 =====')
print()

jogador = dict() # Criando um dicionário vazio
jogadores = list() # Criando uma lista vazia
gols = [] # Criando uma lista vazia

while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).title().strip() # Adicionando o nome do jogador ao dicionário

    jogador['Partidas'] = int(input(f'Quantas Partidas {jogador["Nome"]} jogou? ')) # Adicionando a quantidade de partidas ao dicionário

    # Adicionando valores dos gols a uma lista vazia.
    for i in range(1, jogador['Partidas'] + 1):
        gols.append(int(input(f'  Quantos gols na {i}° partida? ')))
    jogador['Gols'] = gols.copy() # Copiando a lista para o dicionário.
    print()

    jogador['Total'] = sum(gols) # Adicionando a soma de todos os gols ao dicionário.

    jogadores.append(jogador.copy()) # Adicionando todos os valores do dicionário a uma lista.

    gols.clear() # Limpando a lista para a próxima repetição.
    jogador.clear() # Limpando o dicionário para a próxima repetição.

    # Verificando se o usuário deseja adicionar mais dados a lista.
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('Opção inválida!')
    
    if opcao == 'N':
        break
    print()
print()

# Imprimindo a tabela com os dados dos jogadores.
print(f'{"N°":>3} {"NOME":<10} {"GOLS":<18} {"TOTAL":<5}')
print('-' * 40)

# Para imprimir os dados, tive que converter a lista para string, pois a lista era de números inteiros, então não aceitava F-String.
for i in range(len(jogadores)):
    print(f'{i:^3} {jogadores[i]["Nome"]:<10} {str(jogadores[i]["Gols"]):<18} {jogadores[i]["Total"]:^6}')
print('-' * 40)

while True: # Loop para mostrar detalhes dos jogadores.
    while True: # Loop para verificar se o usuário quer ver os detalhes de um jogador.
        print()
        opcao = str(input('Deseja ver os dados de algum jogador? [S/N] ')).upper().strip()[0]
        
        if opcao in 'SN':
            break
        print('Opção inválida!')
    
    # Comando para quebrar o loop principal.
    if opcao == 'N':
        break

    while True: # Loop para verificar se o jogador existe e mostrar os dados.
        print()
        jogador = input('Qual o "Número" do jogador? ').strip()
        
        print()
        if jogador.isnumeric(): # Verificando se um numero foi digitado
            jogador = int(jogador)

            if jogador >= 0 and jogador < len(jogadores): # Verificando se o jogador existe.
                print(f'-- Levantamento do Jogador {jogadores[jogador]["Nome"]} --')
                for i in range(len(jogadores[jogador]['Gols'])):
                    print(f'    No {i + 1}° jogo fez {jogadores[jogador]["Gols"][i]} Gols.')
            else:
                print(f'Jogador "{jogador}" não encontrado!')
        else:
            print(f'"{jogador}" é inválido! Digite um valor numérico.')
        break
print()
