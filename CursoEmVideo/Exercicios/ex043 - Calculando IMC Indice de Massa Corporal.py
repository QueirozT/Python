print('===== EXERCÍCIO #43 =====')
print()

altura = input('Qual a sua altura? ')
peso = input('Qual o seu peso? ')
print()

# Tratamento de erros (simples) para a altura
if str(altura).isdecimal():
    altura = float(altura[:1] + '.' + altura[1:])
else:
    altura = float(altura)

# Tratamento de erros (simples) para o peso
if str(peso).isdecimal():
    peso = float(peso[:2] + '.' + peso[2:])
else:
    peso = float(peso)

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é de: {:.1f}'.format(imc))
    print('Você está abaixo do peso.')
    print()
elif imc < 25:
    print('Seu IMC é de: {:.1f}'.format(imc))
    print('Você está no peso ideal.')
    print()
elif imc < 30:
    print('Seu IMC é de: {:.1f}'.format(imc))
    print('Você está com sobrepeso.')
    print()
elif imc < 40:
    print('Seu IMC é de: {:.1f}'.format(imc))
    print('Você está com obesidade.')
    print()
else:
    print('Seu IMC é de: {:.1f}'.format(imc))
    print('Você está com obesidade mórbida.')
    print()
