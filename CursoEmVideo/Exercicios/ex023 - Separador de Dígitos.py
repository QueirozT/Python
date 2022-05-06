print('===== Exercício 23 =====')
print()

valor = int(input('Digite um número entre 0 e 9999: '))
print()

print('Analisando o número...')
print('O valor digitado foi: {}'.format(valor))

u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print()


# EXEMPLO AVANÇADO (INCOMPLETO):

# print('Unidade: {}'.format(str(valor)[3]))
# print('Dezena: {}'.format(str(valor)[2]))
# print('Centena: {}'.format(str(valor)[1]))
# print('Milhar: {}'.format(str(valor)[0]))
# print()