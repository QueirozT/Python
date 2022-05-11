from datetime import datetime # Tive que importar "datetime" porque a própria biblioteca utiliza uma sub-biblioteca com o mesmo nome.

print('===== EXERCÍCIO #39 =====')
print()

ano = int(input('Informe o seu Ano de nascimento: '))
print()

atual = datetime.now().year
idade = atual - ano

if idade < 18:
    print('Você nasceu em {} e tem {} anos.'.format(ano, idade))
    print('faltam {} anos para você poder se alistar!'.format(18 - idade))
    print()
elif idade == 18:
    print('Você nasceu em {} e tem {} anos.'.format(ano, idade))
    print('Você deve se alistar IMEDIATAMENTE!')
    print()
else:
    print('Você nasceu em {} e tem {} anos.'.format(ano, idade))
    print('Você já deveria ter se alistado há {} anos!'.format(idade - 18))
    print()