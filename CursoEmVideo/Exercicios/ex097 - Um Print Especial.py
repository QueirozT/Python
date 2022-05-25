print('===== EXERCÍCIO #097 =====')
print()

def msg(text):
    print('~' * (len(text) + 10))
    print(f'{text:^{len(text) + 10}}') # As chaves dentro das chaves são para calcular dentro da f-string.
    print('~' * (len(text) + 10))


m = input('Digite uma mensagem para que seja formatada: ')
msg(m)
