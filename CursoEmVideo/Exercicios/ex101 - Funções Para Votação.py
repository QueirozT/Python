print('===== EXERCÍCIO #101 =====')
print()


# Definindo a função que irá retornar a idade e se pode votar ou não.
def votar(ano):
    from datetime import date # Importando a biblioteca dentro da função que vai usa-la, poupa muito espaço de memória.

    idade = date.today().year - ano # Calculando a idade do usuário.
    
    if idade < 16:
        return f'Com {idade} anos, não vota.\n'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos, o vota é opcional.\n'
    else:
        return f'Com {idade} anos, o vota é obrigatório.\n'


# Programa Principal
print('-' * 25)
data = int(input('Em que ano você nasceu? '))

print(votar(data)) # Chamando a função dentro do print().
