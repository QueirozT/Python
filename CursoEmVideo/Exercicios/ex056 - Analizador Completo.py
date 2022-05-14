print('===== EXERCÍCIO #56 =====')
print()

lista = []

# Registrando a lista com nome idade e sexo.
for i in range(4):
    print('{:-^20}'.format(' {}ª PESSOA '.format(i+1)))
    nome = str(input('Nome? '))
    idade = int(input('Idade? '))
    sexo = str(input('Sexo [M/F]? ')).upper()
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
maisVelho = max(homens, key=lambda x: x[1]) # Forma mais simples de se obter o maior valor de uma lista
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


# VERSÃO ALTERNATIVA DO PROGRAMA (Mais simples):

# idadeMedia = 0

# nomeVelho = ''
# idadeVelho = 0

# mulherMenor20 = 0

# for p in range(4):
#     print('{:-^20}'.format(' {}ª PESSOA '.format(p+1)))
#     nome = str(input('Nome: ')).strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('Sexo [M/F]: ')).strip()
#     print()
    
#     idadeMedia += idade

#     if p == 0 and sexo in 'Mm':
#         nomeVelho = nome
#         idadeVelho = idade
#     elif idade > idadeVelho and sexo in 'Mm':
#         nomeVelho = nome
#         idadeVelho = idade

#     if sexo in 'Ff' and idade < 20:
#         mulherMenor20 += 1

# print('A idade média do grupo é {}.'.format(idadeMedia / 4))
# print()

# print('O homem mais velho é {} com {} anos.'.format(nomeVelho, idadeVelho))
# print()

# print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulherMenor20))
# print()
