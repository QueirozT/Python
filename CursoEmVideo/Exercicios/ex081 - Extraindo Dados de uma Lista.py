print('===== EXERCÍCIO #081 =====')
print()

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    while True:
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if resp in 'SN':
            break
        print('Resposta inválida.')
    if resp == 'N':
        break
    print()
 
print()
print(f'Foram digitados {len(lista)} valores.')
print(f'Os valores adicionados em ordem foram: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi digitado.')
print()
