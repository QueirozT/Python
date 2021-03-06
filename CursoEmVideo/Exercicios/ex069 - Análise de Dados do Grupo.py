print('===== EXERCÍCIO #69 =====')
print()

# Iniciando as variáveis (Maior de Idade), (Quantidade de Homens) e (Quantidade de Mulheres)
maior = homem = mulher = 0

while True:
    print('~~' * 10)
    print('CADASTRE UMA PESSOA!')
    print('~~' * 10)

# Coletando a idade da pessoa
    idade = int(input('Idade? '))

# Verificando o sexo da pessoa
    while True:
        nome = str(input('Sexo? [M/F] ')).strip().upper()[0]
        if nome in 'MF':
            break
    print()

# Verificando se é maior de idade e se é homem ou mulher
    if idade >= 18:
        maior += 1
    if nome == 'M':
        homem += 1
    if nome == 'F' and idade < 20:
        mulher += 1

# Verificando se o usuário quer continuar ou não
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print()

        if opcao in 'S':
            break
        elif opcao in 'N':
            break
    if opcao == 'N':
        break

# Mostrando os resultados
print('~~' * 30)
if maior == 0:
    print('{:^60}'.format('Não há pessoas com mais de 18 anos!'))
elif maior == 1:
    print('{:^60}'.format('Você cadastrou uma pessoa com mais de 18 anos.'))
else:
    print('{:^60}'.format(f'Você cadastrou {maior} pessoas com mais de 18 anos.'))

if homem == 0:
    print('{:^60}'.format('Não há homens cadastrados.'))
elif homem == 1:
    print('{:^60}'.format('Ao todo temos apenas uma pessoa do sexo masculino.'))
else:
    print('{:^60}'.format(f'Ao todo temos {homem} pessoas do sexo masculino.'))

if mulher == 0:
    print('{:^60}'.format('Não temos nenhuma mulher com menos de 20 anos.'))
elif mulher == 1:
    print('{:^60}'.format('Temos apenas uma pessoa do sexo feminino com menos de 20 anos.'))
else:
    print('{:^60}'.format(f'Temos {mulher} pessoas do sexo feminino com menos de 20 anos.'))
print('~~' * 30)
print()
