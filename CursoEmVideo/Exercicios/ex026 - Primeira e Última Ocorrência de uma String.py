print('===== Exercício 26 =====')
print()

valor = input('Digite uma frase: ')
print()

print('A letra "A" aparece {} vezes na frase.'.format(valor.upper().count('A')))
print()

print('A primeira letra "A" aparece na posição {}.'.format(valor.upper().find('A')))
print()

print('A última letra "A" aparece na posição {}.'.format(valor.upper().rfind('A'))) # O .rfind() é o mesmo que o .find(), porém, começa a busca do último caractere.