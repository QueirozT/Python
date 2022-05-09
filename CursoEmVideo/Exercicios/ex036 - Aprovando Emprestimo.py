print('===== EXERCÍCIO #36 =====')
print()

valor = float(input('Informe o valor do imóvel que deseja comprar: R$'))
salario = float(input('Informe o valor do seu salário: R$'))
tempo = int(input('Informe em quantos anos deseja financiar: '))
print()

prestacao = valor / (tempo * 12)

if salario * 0.3 > prestacao:
    print('O emprestimo foi aprovado!')
    print('O valor da prestação será de R${:.2f} por {:.0f} meses ou {:.0f} anos'.format(prestacao, tempo * 12, tempo))
    print()
else:
    print('O emprestimo foi negado!')
    print()
