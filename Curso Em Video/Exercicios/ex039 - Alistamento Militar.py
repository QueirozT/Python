from datetime import datetime # Tive que importar "datetime" porque a própria biblioteca utiliza uma sub-biblioteca com o mesmo nome.
# from datetime import date # Opcional, pois a função 'date' só trabalha com datas.

print('===== EXERCÍCIO #39 =====')
print()

ano = int(input('Informe o seu Ano de nascimento: '))
print()

atual = datetime.now().year 
# atual = date.today().year # Retorna o ano atual.

idade = atual - ano

if idade < 18:
    print('Você nasceu em {} e tem {} anos.'.format(ano, idade))
    if 18 - idade == 1:
        print('Falta 1 ano para você poder se alistar!')
    else:
        print('Faltam {} anos para você poder se alistar!'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
    print()
elif idade == 18:
    print('Você nasceu em {} e tem {} anos.'.format(ano, idade))
    print('Você deve se alistar IMEDIATAMENTE!')
    print()
else:
    print('Você nasceu em {} e tem {} anos.'.format(ano, idade))
    print('Você já deveria ter se alistado há {} anos!'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(atual - (idade - 18)))
    print()
