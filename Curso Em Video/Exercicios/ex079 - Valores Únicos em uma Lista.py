print('===== EXERCÍCIO #079 =====')
print()

lista = []

while True:
    while True: # Laço para verificar se o valor digitado é um número inteiro.
        valor = input('Digite um valor: ').strip()
        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print('Valor inválido!')
            print()
    
    if not valor in lista: # Condicional para verificar se o valor digitado já existe na lista e adicionar.
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    print()

    while True: # Laço para verificar se o usuário deseja continuar ou não.
        opcao = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if opcao in 'SN':
            print()
            break
        else:
            print('Opção inválida!')
            print()
    if opcao == 'N':
        break

lista.sort() # Re-ordena a lista.

print(f'Os valores digitados foram: {lista}')
print()
