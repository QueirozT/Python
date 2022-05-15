print('===== EXERCÍCIO #63 =====')
print()

quantidade = int(input('Quantos elementos você quer mostrar? '))
print()

resultado = 1
anterior = 1

while quantidade != 0:
    print('{}'.format(resultado), end=' -> ')
    resultado += anterior
    anterior = resultado - anterior
    quantidade -= 1
print('FIM!')
print()
