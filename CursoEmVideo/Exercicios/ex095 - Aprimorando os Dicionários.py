print('===== EXERCÍCIO #095 =====')
print()

jogador = dict() # Criando um dicionário vazio
time = list() # Criando uma lista vazia
partidas = [] # Criando uma lista vazia

while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).title().strip() # Adicionando o nome do jogador ao dicionário

    jogador['Partidas'] = int(input(f'Quantas Partidas {jogador["Nome"]} jogou? ')) # Adicionando a quantidade de partidas ao dicionário

    # Adicionando valores dos gols a uma lista vazia.
    for i in range(1, jogador['Partidas'] + 1):
        partidas.append(int(input(f'  Quantos gols na {i}° partida? ')))
    jogador['Gols'] = partidas.copy() # Copiando a lista para o dicionário.
    print()

    jogador['Total'] = sum(partidas) # Adicionando a soma de todos os gols ao dicionário.

    time.append(jogador.copy()) # Adicionando todos os valores do dicionário a uma lista.

    partidas.clear() # Limpando a lista para a próxima repetição.
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

# Imprimindo a tabela com os dados do time.
print(f'{"N°":>3} {"NOME":<10} {"GOLS":<18} {"TOTAL":<5}')
print('-' * 40)

# Para imprimir os dados, tive que converter a lista para string, pois a lista era de números inteiros, então não aceitava F-String.
for i in range(len(time)):
    print(f'{i:^3} {time[i]["Nome"]:<10} {str(time[i]["Gols"]):<18} {time[i]["Total"]:^6}')
print('-' * 40)

while True: # Loop para mostrar detalhes do time.
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
        
        if jogador.isnumeric(): # Verificando se um numero foi digitado
            jogador = int(jogador)

            if jogador >= 0 and jogador < len(time): # Verificando se o jogador existe.
                print(f'-- Levantamento do Jogador {time[jogador]["Nome"]} --')
                for i in range(len(time[jogador]['Gols'])):
                    print(f'    No {i + 1}° jogo fez {time[jogador]["Gols"][i]} Gols.')
            else:
                print(f'Jogador "{jogador}" não encontrado!')
        else:
            print(f'"{jogador}" é inválido! Digite um valor numérico.')
        break
print()
