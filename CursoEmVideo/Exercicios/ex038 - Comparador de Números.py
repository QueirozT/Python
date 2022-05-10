print('===== EXERCÍCIO #38 =====')
print()

val01 = int(input('Insira o primeiro número: '))
val02 = int(input('Insira o segundo número: '))
print()

if val01 > val02:
    print('"{}" é maior que "{}"!'.format(val01, val02))
    print()
elif val01 < val02:
    print('"{}" é maior que "{}"!'.format(val02, val01))
    print()
else:
    print('Os dois valores são iguais!'.format(val01, val02))
    print()
