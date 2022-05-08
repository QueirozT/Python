from datetime import date

print('===== EXERCÍCIO 32 =====')
print()

valor = input('Que ano quer analizar? Coloque "0" para analizar o ano atual: ')
print()

if int(valor) == 0:
    valor = str(date.today().year)

# Se o valor for divisível por 4 e (não for divisível por 100 /ou for divisível 400), significa que é bissexto!
if valor.isnumeric():
    if int(valor) % 4 == 0 and int(valor) % 100 != 0 or int(valor) % 400 == 0:
        print('O ano "{}" é bissexto!'.format(valor))
        print()
    else:
        print('O ano "{}" não é bissexto!'.format(valor))
        print()
else:
    print('"{}" é um valor inválido!'.format(valor))
    print()
