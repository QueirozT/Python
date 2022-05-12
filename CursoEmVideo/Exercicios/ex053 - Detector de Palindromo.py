print('===== EXERCÍCIO #53 =====')
print()

frase = str(input('Digite uma frase: ')).strip().upper() # Remove os espaços em branco no início e no fim e transforma a frase em MAIUSCULA.

frase = ''.join(frase.split()) # Remove os espaços em branco entre as palavras.

teste = frase[::-1] # Inverte a frase.

if frase == teste: # Verifica se a frase é um palíndromo comparando ela mesma ao contrário.
    print('{}'.format(frase))
    print('É um palíndromo!')
else:
    print('{}'.format(frase))
    print('Não é um palíndromo!')
print()
