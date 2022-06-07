print('===== EXERCÍCIO 010 =====')
print()

valor = float(input('Quantos reais você tem? '))
print()

print('Você tem R$ {:.2f} Reais, o valor do dólar atual é US$ {:.2f} você pode comprar US$ {:.2f} Dólares.'.format(valor, 4.91, valor / 4.91))
