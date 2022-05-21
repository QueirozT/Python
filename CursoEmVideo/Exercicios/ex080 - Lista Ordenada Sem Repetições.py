print('===== EXERCÍCIO #080 =====')
print()

lista = list() # Cria uma lista vazia

for c in range(5):
    valor = int(input('Digite um valor: '))

    if c == 0 or valor > lista[-1]: # Verifica se é o primeiro valor ou se é maior que o último da lista.
        lista.append(valor)
        print('Adicionado ao final da lista.')
    else:
        for i in lista: # Pega cada item "i" da lista.
            if valor <= i:
                lista.insert(lista.index(i), valor) 
                print(f'Adicionado a posição {lista.index(valor)} da lista.')
                break
    print()

print(f'Os valores adicionados em ordem foram: {lista}')
print()


# VERSÃO ALTERNATIVA DO PROGRAMA:

# lista = [] # Cria uma lista vazia

# for i in range(5):
#     valor = int(input('Digite um valor: '))

#     if i == 0 or valor >= lista[-1]: # Verifica se é o primeiro valor ou se é maior que o último da lista.
#         lista.append(valor)
#         print('Adicionado ao final da lista.')
#     else:
#         for i, v in enumerate(lista): # Pega a posição "i" e o valor "v" de cada item da lista.
#             if valor <= v:
#                 lista.insert(i,valor)
#                 print(f'Adicionado na posição {i} da lista.')
#                 break
#     print()

# print(f'Os valores adicionados em ordem foram: {lista}')
# print()
