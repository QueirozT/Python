print('===== EXERCÍCIO #43 =====')
print()

altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
print()

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('Você está abaixo do peso.')
    print()
elif imc < 25:
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('Você está no peso ideal.')
    print()
elif imc < 30:
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('Você está com sobrepeso.')
    print()
elif imc < 40:
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('Você está com obesidade.')
    print()
else:
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('Você está com obesidade mórbida.')
    print()
