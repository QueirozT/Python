print('===== Exercício 26 =====')
print()

valor = str(input('Digite uma frase: ')).strip()
print()

print('A letra "A" aparece {} vezes na frase.'.format(valor.upper().count('A')))
print()

print('A primeira letra "A" aparece na posição {}.'.format(valor.upper().find('A') + 1))
print()

print('A última letra "A" aparece na posição {}.'.format(valor.upper().rfind('A') + 1))
print()