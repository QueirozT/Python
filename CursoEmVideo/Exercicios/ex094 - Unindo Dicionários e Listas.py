print('===== EXERCÍCIO #094 =====')
print()

pessoa = dict()
lista = list()

while True:
    pessoa['Nome'] = str(input('Nome: ')).title().strip()
    print()

    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas Masculino "M" ou Feminino "F".')
    print()

    pessoa['Idade'] = int(input('Idade: '))
    print()

    lista.append(pessoa.copy())

    pessoa.clear()

    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print(f'"{opcao}" não é uma opção válida. Por favor, digite apenas Sim "S" ou Não "N".')
    
    if opcao == 'N':
        break
    print()
print()

print('-=-' * 30)
print()

print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
print()

media = sum(pessoa['Idade'] for pessoa in lista) / len(lista) # Forma resumida de fazer um for através do método sum()
print(f'A média de idade é de {media:.0f} anos.')
print()

print('As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['Sexo'] == 'F':
        print(f' {p["Nome"]}; ', end='')
print('\n')

print('Lista das pessoas que estão acima da média: ')
print(f'  {"NOME":^10} | {"SEXO":^8} | {"IDADE":^8}')
for p in lista:
    if p['Idade'] > media:
        print(f'  {p["Nome"]:^10} | {p["Sexo"]:^8} | {p["Idade"]:^8}')
print()
