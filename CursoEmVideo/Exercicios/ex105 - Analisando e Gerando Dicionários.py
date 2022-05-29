print('===== EXERCÍCIO #105 =====')
print()


def analisar(tupla, sit=False):
    """
    -> Função para receber uma tupla com várias notas e retornar um dicionário com a análise de dados.
    :tupla = Tupla com várias notas (Poderia ser um empacotador (* num), mas no final também retornaria uma tupla com as notas).
    :sit = (Opcional) Mostrar uma análise da situação do aluno baseada nas notas fornecidas.
    :return: Dicionário com as informações da situação do aluno.
    # Criado por Tiago.
    """
    aluno = dict()

    aluno['Total'] = len(tupla)
    aluno['Maior'] = max(tupla)
    aluno['Menor'] = min(tupla)
    aluno['Média'] = sum(tupla) / len(tupla)
    
    if sit:
        if aluno['Média'] >= 7:
            aluno['Situação'] = 'Aprovado'
        elif aluno['Média'] >= 5:
            aluno['Situação'] = 'Recuperação'
        else:
            aluno['Situação'] = 'Reprovado'
    
    return aluno


# programa Principal
notas = ()

while True:
    notas += (float(input('Digite uma nota: ')),)
    
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Opção Inválida!')
    if resp in 'N':
        break
print()

while True:
    opcao = input('Deseja ver a situação do aluno? [S/N] ').strip().upper()[0]
    if opcao in 'SN':
        break
    print('Opcão inválida!')
print()

if opcao in 'S':
    opcao = True
else:
    opcao = False

print(analisar(notas, opcao))
print()
