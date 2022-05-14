print('===== EXERCÍCIO #57 =====')
print()

sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
    if sexo != 'F' and sexo != 'M':
        print('"{}" não é um valor válido. Tente novamente!'.format(sexo))
print('Sexo "{}" registrado com sucesso!'.format(sexo))
print()
