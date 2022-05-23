print('===== EXERCÍCIO #093 =====')
print()

# Inicializando as variáveis
jogador = dict()
Gols = list()

# Coletando o Nome e adicionando a biblioteca.
jogador['Nome'] = str(input('Qual o nome do jogador? '))
print()

# Coletando a quantidade de partidas para iniciar o loop.
totalGols = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

# Iniciando o loop para coletar os gols.
for i in range(1, totalGols + 1):
    Gols.append(int(input(f'Quantos gols na {i}° partida? ')))

# Adicionando a lista de gols e a quantidade de partidas ao dicionário.
jogador['Gols'] = Gols.copy() # Copiando a lista para não alterar a original.
jogador['Partidas'] = totalGols
print()

print('-=-' * 30)
print()

# Imprimindo o dicionário sem formatação.
print(jogador)
print()

print('-=-' * 30)
print()

# Imprimindo o dicionário com formatação simples, Key e Valor.
for k, v in jogador.items():
    print(f'O campo {k} tem o valor "{v}"')
print()

print('-=-' * 30)
print()

# Imprimindo o dicionário com formatação mais complexa, Varrendo a lista dentro do dicionário e imprimindo os Valores.
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for i in range(len(jogador['Gols'])):
    print(f'  => Na {i + 1}° partida, fez {jogador["Gols"][i]} gols.')
print(f'Foi um total de {sum(jogador["Gols"])} gols.')
print()
