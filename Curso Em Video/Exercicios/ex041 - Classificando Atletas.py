from datetime import date

print('===== EXERCÍCIO #41 =====')
print()

ano = int(input('Qual seu ano de nascimento? '))
print()

idade = date.today().year - ano

if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: MIRIM')
    print()
elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: INFANTIL')
    print()
elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: JUNIOR')
    print()
elif idade <= 20:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: SÊNIOR')
    print()
else:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: MASTER')
    print()
