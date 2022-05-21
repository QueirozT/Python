print('===== EXERCÍCIO #082 =====')
print()

# Inicializando as variáveis. Ps: As listas não podem ser inicializadas juntas, porque acabam referenciando o mesmo espaço na memória.
lista = list()
par = []
impar = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor) # Adicionando o valor na lista principal

# Verificando se o valor é par ou impar e adicionando na lista correspondente.
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

# Verificando se o usuário quer continuar
    while True:
        opcao = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if opcao in 'SN':
            break
        print('Resposta inválida!')
    print()

    if opcao == 'N':
        break

print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
print()
