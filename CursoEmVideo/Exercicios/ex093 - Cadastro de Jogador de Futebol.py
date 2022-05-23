print('===== EXERCÍCIO #093 =====')
print()

jogador = dict()
Gols = list()

jogador['Nome'] = str(input('Qual o nome do jogador? '))
print()

totalGols = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for i in range(1, totalGols + 1):
    Gols.append(int(input(f'Quantos gols na {i}° partida? ')))

jogador['Gols'] = Gols.copy()
jogador['Partidas'] = totalGols
print()

print('-=-' * 30)
print()

print(jogador)
print()

print('-=-' * 30)
print()

for k, v in jogador.items():
    print(f'O campo {k} tem o valor "{v}"')
print()

print('-=-' * 30)
print()

print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for i in range(len(jogador['Gols'])):
    print(f'  => Na {i + 1}° partida, fez {jogador["Gols"][i]} gols.')
print(f'Foi um total de {sum(jogador["Gols"])} gols.')
print()
