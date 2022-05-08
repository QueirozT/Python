print('===== EXERCÍCIO 29 =====')
print()

valor = float(input('A quantos km/h você está? '))
print()

if valor > 80:
    print('MULTADO! Você está acima do limite de velocidade que é 80km/h')
    print('Você deve pagar a multa no valor de R${:.2f}'.format((valor - 80) * 7))
    print()
    
print('Tenha um bom dia! Dirija com segurança!')
print()
