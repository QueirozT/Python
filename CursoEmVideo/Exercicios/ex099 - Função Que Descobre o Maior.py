from time import sleep

print('===== EXERCÍCIO #099 =====')
print()

# Definindo "def" uma função para mostrar o maior número.
def maior(* val):
    print('-=-' * 10)
    print('Analizando os valores passados...')
    sleep(2)

    if len(val) == 0: # Se não tiver nenhum valor, retorna a mensagem abaixo.
        print('Foram informados 0 valores.')
        print('O maior valor informado foi 0.')
    else:
        print(f'Foram informados {len(val)} valores, e foram: ', end='')
        for i in val:
            print(i, end=' ', flush=True)
            sleep(0.5)
        print()

        print(f'O maior valor informado foi {max(val)}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print()
