print('===== EXERCÍCIO #072 =====')
print()

lista = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    valor = input('Digite um valor entre 0 e 20: ')
    if valor.isnumeric() and int(valor) >= 0 and int(valor) <= 20:
        valor = int(valor)
        break
    else:
        print('Valor inválido!')
    print()

print(f'Você digitou o número "{lista[valor]}"')
print()
