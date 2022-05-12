print('===== EXERCÍCIO #56 =====')
print()

lista = []

# Registrando a lista com nome idade e sexo.
for i in range(0, 4):
    nome = str(input('Qual é o nome? '))
    idade = int(input('Qual é a idade? '))
    sexo = str(input('Qual o sexo "M" ou "F"? ')).upper()
    lista += [[nome, idade, sexo]]
    print()
print()

# Calculando a média de idade
idade = 0
for i in range(0, len(lista)):
    idade += int(lista[i][1])

print('A média de idade do grupo é {}'.format(idade / len(lista)))
print()

# Separando os homens
homens = []
for i in range(0, len(lista)):
    if lista[i][2] == 'M':
        homens += [lista[i]]

# Calculando a média de idade dos homens
maisVelho = max(homens, key=lambda x: x[1])
print('O homem mais velho é {} com {} anos'.format(maisVelho[0], maisVelho[1]))
print()

# Calculando quantas mulheres tem menos de 20 anos
mulheres = 0
for i in range(0, len(lista)):
    if lista[i][2] == 'F' and lista[i][1] < 20:
        mulheres += 1

if mulheres > 0:
    print('A quantidade de mulheres com menos de 20 anos é {}'.format(mulheres))
else:
    print('Não existe mulher com menos de 20 anos na lista.')
print()
