from datetime import date

print('===== EXERCÍCIO #092 =====')
print()

# Criando um dicionário vazio.
trabalhador = {}

# Coletando os dados do trabalhador.
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
trabalhador['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['Carteira de Trabalho'] > 0:
    trabalhador['Ano de Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = float(input('Salario: R$'))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + 35 - (date.today().year - trabalhador['Ano de Contratação'])
print()

print('-=' * 30)
print()

for k, v in trabalhador.items(): # Varrendo o dicionário e personalizando a saída com F-Strings e condicionáis simplificadas.
    print(f'{"O" if k in "Nome Ano de Contratação Salário" else "A"} {k} é {"Com " if k in "Aposentadoria" else ""}{f"R${v:.2f}" if k in "Salário" else v } {"Anos" if k in "Aposentadoria Idade" else ""}')
print()
