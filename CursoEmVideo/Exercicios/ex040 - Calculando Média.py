print('===== EXERCÍCIO #40 =====')
print()

nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
print()

media = (nota01 + nota02) / 2

if media < 5:
    print('Sua média é: {:.1f} \nVocê está REPROVADO!'.format(media))
    print()
elif media < 6.9:
    print('Sua média é: {:.1f} \nVocê está de RECUPERAÇÃO!'.format(media))
    print()
else:
    print('Sua média é: {:.1f} \nVocê está APROVADO!'.format(media))
    print()
