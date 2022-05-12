print('===== EXERCÍCIO #43 =====')
print()

altura = input('Qual a sua altura? ')
peso = input('Qual o seu peso? ')
print()

# Tratamento de erros (simples) para identificar se algum caractere não numérico foi inserido.
if str(altura).isalpha() or str(peso).isalpha():
    numero = False
else:
    numero = True

# Tratamento de erros (simples) para a conversão da altura.
if numero:
    if str(altura).isdecimal():
        altura = float(altura[:1] + '.' + altura[1:])
    else:
        altura = float(altura)

# Tratamento de erros (simples) para a conversão do peso.
if numero:
    if str(peso).isdecimal():
        peso = float(peso[:2] + '.' + peso[2:])
    else:
        peso = float(peso)

if numero:
    imc = peso / (altura * altura)


if numero:
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
else:
    print('Não é possível calcular o IMC com esses dados.')
    print()
