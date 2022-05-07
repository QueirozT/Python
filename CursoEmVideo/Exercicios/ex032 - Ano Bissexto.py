print('===== EXERCÍCIO 32 =====')
print()

valor = input('Digite o ano que você deseja saber se é bissexto: ')
print()

if valor.isnumeric():
    if int(valor) % 4 == 0: # Se o resto da divisão por 4 for 0, o ano é bissexto.
        print('O ano "{}" é bissexto!'.format(valor))
        print()
    else:
        print('O ano "{}" não é bissexto!'.format(valor))
        print()
else:
    print('"{}" é um valor inválido!'.format(valor))
    print()
