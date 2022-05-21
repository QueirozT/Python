print('===== EXERCÍCIO #080 =====')
print()

lista = list()

for i in range(5):
    valor = int(input('Digite um valor: '))

    if i == 0:
        lista.append(valor)
        print('Primeiro valor adicionado a lista.')
    elif valor >= lista[-1]:
        lista.append(valor)
        print('Valor adicionado ao final da lista.')
    elif valor <= lista[0]:
        lista.insert(0, valor)
        print('Valor adicionado a posição 0.')
    elif valor > lista[0] and valor <= lista[1]:
        lista.insert(1, valor)
        print('Valor adicionado a posição 1.')
    elif valor > lista[1] and valor <= lista[2]:
        lista.insert(2, valor)
        print('Valor adicionado a posição 2.')
    elif valor > lista[2] and valor <= lista[3]:
        lista.insert(3, valor)
        print('Valor adicionado a posição 3.')
    elif valor > lista[3] and valor <= lista[4]:
        lista.insert(4, valor)
        print('Valor adicionado a posição 4.')
    print()

print(f'Os valores adicionados em ordem foram: {lista}')
print()
