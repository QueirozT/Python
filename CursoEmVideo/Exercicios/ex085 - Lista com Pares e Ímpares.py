print('===== EXERCÍCIO #085 =====')
print()

lista = [[],[]] # Criando uma lista composta com duas listas vazias.

for i in range(7):
    valor = int(input(f'Digite o {i + 1}º número: '))
    print()

    if valor % 2 == 0: # Verificando se o valor é par ou impar e adicionando na lista correspondente.
        lista[0].append(valor)
    else:
        lista[1].append(valor)

# Alterando a sequência de valores da lista composta.
lista[0].sort()
lista[1].sort()

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
print()
