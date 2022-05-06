print('===== Exercício 23 =====')
print()

valor = int(input('Digite um número entre 0 e 9999: '))
print()

print('O valor digitado foi: {}'.format(valor))

print('Ele contém:')

print('Unidade: {}'.format(str(valor)[3]))
print('Dezena: {}'.format(str(valor)[2]))
print('Centena: {}'.format(str(valor)[1]))
print('Milhar: {}'.format(str(valor)[0]))
print()


# EXEMPLO MATEMÁTICO

# print('Unidade: {}'.format(valor % 10))
# print('Dezena: {}'.format(valor % 100 // 10))
# print('Centena: {}'.format(valor % 1000 // 100))
# print('Milhar: {}'.format(valor // 1000))
# print()