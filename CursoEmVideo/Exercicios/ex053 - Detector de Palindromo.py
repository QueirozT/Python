print('===== EXERCÍCIO #53 =====')
print()

frase = str(input('Digite uma frase: ')).strip().upper()

frase = ''.join(frase.split())

teste = frase[::-1]

if frase == teste:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
print()
