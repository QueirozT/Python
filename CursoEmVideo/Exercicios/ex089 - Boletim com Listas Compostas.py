print('===== EXERCÍCIO #089 =====')
print()

lista = list()

while True:
    nome = input('Nome? ')
    nt1 = float(input('1° Nota? '))
    nt2 = float(input('2° Nota? '))
    media = (nt1 + nt2) / 2

    lista.append([nome, nt1, nt2, media])

    while True:
        opcao = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if opcao in 'SN':
            break
        print('Opção inválida!')
    print()

    if opcao == 'N':
        break

print(f'{f"N°":<5}{f"NOME":<10}{f"MÉDIA":>12}')
print('~' * 30)

for i, v in enumerate(lista):
    print(f'{i+1:<5}{v[0]:<10}{v[3]:>12.1f}')

print('~' * 30)
print()

while True:
    while True:
        opcao = str(input(f'Deseja ver a nota de algum aluno? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('Opção inválida!')
        print()
    
    if opcao in 'N':
        break
    
    aluno = str(input('Qual o Nome ou o N° do aluno? ')).upper().strip()
    if aluno.isnumeric():
        aluno = int(aluno) - 1
        print(f'\nAs notas de {lista[aluno][0]} são {lista[aluno][1]} e {lista[aluno][2]} a média é {lista[aluno][3]:.1f}')
    else:
        for i, v in enumerate(lista):
            if aluno == v[0].upper():
                print(f'\nAs notas de {v[0]} são {v[1]} e {v[2]} a média é {v[3]:.1f}')
                break
            elif i == len(lista) - 1:
                print('\nAluno não encontrado!')
    print()
print()
