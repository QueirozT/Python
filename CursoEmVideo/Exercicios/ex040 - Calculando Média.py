print('===== EXERCÍCIO #40 =====')
print()

nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
print()

media = (nota01 + nota02) / 2

if media < 5:
    print('Sua média é: {:.1f} \nVocê está {}REPROVADO!{}'.format(media, '\033[31m', '\033[m'))
    print()
elif media < 6.9:
    print('Sua média é: {:.1f} \nVocê está de {}RECUPERAÇÃO!{}'.format(media, '\033[34m', '\033[m'))
    print()
else:
    print('Sua média é: {:.1f} \nVocê está {}APROVADO!{}'.format(media, '\033[32m', '\033[m'))
    print()
