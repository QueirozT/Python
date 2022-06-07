print('===== EXERCÍCIO 30 =====')
print()

valor = input('Digite um valor: ')
print()

if valor.isdecimal():
    if int(valor) % 2 == 0:
        print('"{}" é par!'.format(valor))
    else:
        print('"{}" é ímpar!'.format(valor))
    print()
elif valor.isalpha() or valor.isalnum():
    print('Para funcionar, precisamos de um número. "{}" não é um número!'.format(valor))
    print()
else:
    print('Não é possível determinar se "{}" é Par ou Ímpar!'.format(valor))
    print('Digite um valor acima de 0 sem ponto flutuante!')
    print()

