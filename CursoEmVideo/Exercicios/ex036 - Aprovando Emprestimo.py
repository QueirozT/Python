print('===== EXERCÍCIO #36 =====')
print()

valor = float(input('Informe o valor do imóvel que deseja comprar: R$'))
salario = float(input('Informe o valor do seu salário: R$'))
tempo = int(input('Informe em quantos anos deseja financiar: '))
print()

prestacao = valor / (tempo * 12)

if salario * 0.3 > prestacao:
    print('Para financiar uma casa de R${:.2f} O valor da prestação será de R${:.2f} por {:.0f} meses'.format(valor, prestacao, tempo * 12))
    print('O emprestimo foi aprovado!')
    print()
else:
    print('Para financiar uma casa de R${:.2f} em {:.0f} anos, o valor da prestação será de R${:.2f} por mês'.format(valor, tempo, prestacao))
    print('O emprestimo foi negado!')
    print()
