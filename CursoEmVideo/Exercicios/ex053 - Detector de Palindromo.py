print('===== EXERCÍCIO #53 =====')
print()

frase = str(input('Digite uma frase: ')).strip().upper() # Remove os espaços em branco no início e no fim e transforma a frase em MAIUSCULA.
print()

frase = ''.join(frase.split()) # Remove os espaços em branco entre as palavras.

aoContrario = frase[::-1] # Inverte a frase.

print('O  inverso de {} é {}.'.format(frase, aoContrario))

if frase == aoContrario: # Verifica se a frase é um palíndromo comparando ela mesma ao contrário.
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
print()


# VERSÃO ALTERNATIVA USANDO O FOR:

# frase = str(input('Escreva uma frase: ')).strip().upper()
# print()

# frase = ''.join(frase.split())

# inverso = ''

# for letra in range(len(frase) - 1, -1, -1):
#     inverso += frase[letra]

# print('O inverso de {} é {}.'.format(frase, inverso))

# if frase == inverso:
#     print('Temos um palíndromo!')
# else:
#     print('A frase digitada não é um palíndromo!')
# print()
