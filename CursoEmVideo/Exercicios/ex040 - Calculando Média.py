print('===== EXERCÍCIO #40 =====')
print()

nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
print()

media = (nota01 + nota02) / 2

if media < 5:
    print('Com {:.1f} e {:.1f} a Sua média é: {:.1f} \nVocê está {}REPROVADO!{}'.format(nota01, nota02, media, '\033[31m', '\033[m'))
    print()
elif media < 6.9:
    print('Com {:.1f} e {:.1f} a Sua média é: {:.1f} \nVocê está em {}RECUPERAÇÃO!{}'.format(nota01, nota02, media, '\033[34m', '\033[m'))
    print()
else:
    print('Com {:.1f} e {:.1f} a Sua média é: {:.1f} \nVocê está {}APROVADO!{}'.format(nota01, nota02, media, '\033[32m', '\033[m'))
    print()

# Eu poderia poupar código retirando a média e imprimindo antes das condicionais, mas quero mostrar também o uso do \n
