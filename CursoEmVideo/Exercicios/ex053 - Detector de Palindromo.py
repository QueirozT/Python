print('===== EXERCÍCIO #53 =====')
print()

frase = str(input('Digite uma frase: ')).strip().upper() # Remove os espaços em branco no início e no fim e transforma a frase em MAIUSCULA.
print()

semEspaco = ''.join(frase.split()) # Remove os espaços em branco entre as palavras.

aoContrario = semEspaco[::-1] # Inverte a frase.

if semEspaco == aoContrario: # Verifica se a frase é um palíndromo comparando ela mesma ao contrário.
    print('{}'.format(frase))
    print('É UM PALÍNDROMO!')
else:
    print('{}'.format(frase))
    print('Não É UM PALÍNDROMO!')
print()
