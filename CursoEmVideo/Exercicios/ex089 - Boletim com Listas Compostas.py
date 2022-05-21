print('===== EXERCÍCIO #089 =====')
print()

lista = list() # Lista Vazia.

while True:
    nome = input('Nome? ')
    nt1 = float(input('1° Nota? '))
    nt2 = float(input('2° Nota? '))
    media = (nt1 + nt2) / 2

    lista.append([nome, nt1, nt2, media]) # Adicionando os dados coletados em formato de lista Para criar uma lista composta.

    while True:
        opcao = input('Deseja continuar? [S/N] ').upper().strip()[0] # verificando se quer adicionar mais alunos a lista composta.
        if opcao in 'SN':
            break
        print('Opção inválida!')
    print()

    if opcao == 'N':
        break

print(f'{f"N°":<5}{f"NOME":<10}{f"MÉDIA":>12}') # Formatando o cabeçalho da tabela.
print('~' * 30)

for i, v in enumerate(lista):
    print(f'{i+1:<5}{v[0]:<10}{v[3]:>12.1f}') # Imprimindo os dados da lista composta formatados na tabela.

print('~' * 30)
print()

while True:
    while True:
        opcao = str(input(f'Deseja ver a nota de algum aluno? [S/N] ')).upper().strip()[0] # Verificando se quer ver a nota de algum aluno.
        if opcao in 'SN':
            break
        print('Opção inválida!')
        print()
    
    if opcao in 'N':
        break
    
    aluno = str(input('Qual o Nome ou o N° do aluno? ')).upper().strip() # Coletando o nome ou o número do aluno.
    if aluno.isnumeric() and int(aluno) <= len(lista): # verificando se um número foi digitado e se é menor que o tamanho da lista.
        aluno = int(aluno) - 1
        print(f'\nAs notas de {lista[aluno][0]} são {lista[aluno][1]} e {lista[aluno][2]} a média é {lista[aluno][3]:.1f}')
    else:
        for i, v in enumerate(lista):
            if aluno == v[0].upper(): # verificando se o nome digitado é igual ao nome do aluno na lista.
                print(f'\nAs notas de {v[0]} são {v[1]} e {v[2]} a média é {v[3]:.1f}')
                break
            elif i == len(lista) - 1:
                print('\nAluno não encontrado!')
    print()
print()
