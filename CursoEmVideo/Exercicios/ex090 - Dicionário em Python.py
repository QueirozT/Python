print('===== EXERCÍO #090 =====')
print()

aluno = dict() # Cria um dicionário vazio

# Adiciona os valores ao dicionário
aluno['Nome'] = str(input('Qual o nome do aluno? ')).strip().title()
aluno['Média'] = float(input(f'Qual a média de {aluno["Nome"]}? '))
print()

# Verificando se o aluno foi aprovado ou reprovado e armazenando no dicionário.
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação!'
else:
    aluno['Situação'] = 'Reprovado!'

# Varrendo o dicionário e exibindo os valores.
for k, v in aluno.items(): # Varrendo os valores Key 'k' e Value 'v' do dicionário.
    print(f'{k} é {v}') # Imprimindo as Chaves e os Valores.
print()
