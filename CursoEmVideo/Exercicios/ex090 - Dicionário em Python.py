print('===== EXERCÍO #090 =====')
print()

aluno = dict()

aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input('Média: '))
print()

if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado!'
else:
    aluno['Situação'] = 'Aprovado!'

for i, v in aluno.items():
    print(f'{i} é {v}')
print()
