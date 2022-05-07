print('===== EXERCÍCIO 29 =====')
print()

print('Esta é uma via de 80km/h.')
valor = float(input('A quantos km/h você está? '))
print()

if valor > 80:
    print('Você está acima da velocidade!')
    print('Uma multa no valor de R${:.2f} foi gerada.'.format((valor - 80) * 7))
    print('Dirija com cuidado!')
else:
    print('Parabéns, você está dentro da velocidade!')
print()
