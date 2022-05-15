print('===== EXERCÍCIO #65 =====')
print()

maior = menor = contador = soma = 0 # Inicializando multiplas variáveis

opcao = 'S'

while opcao == 'S':
    valor = int(input('Digite um valor: '))
    print()

    if contador == 0:
        maior = menor = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    
    soma += valor
    
    contador += 1
    
    opcao = input('Quer continuar? [S/N] ').upper().strip()
    print()

print('A média dos {} valores digitados é {:.1f}'.format(contador, (soma / contador)))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
print()
