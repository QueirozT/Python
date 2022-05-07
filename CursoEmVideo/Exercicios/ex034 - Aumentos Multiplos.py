print('===== EXERCÍCIO 34 =====')
print()

valor = float(input('Qual o valor do seu salário? R$'))
print()

if valor > 1250:
    print('Parabéns, você recebeu um aumento de 10%, seu salário agora é de R${:.2f}!'.format(valor + valor * 0.10))
    print()
else:
    print('Parabéns, você recebeu um aumento de 15%, seu salário agora é de R${:.2f}!'.format(valor + valor * 0.15))
    print()
