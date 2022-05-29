from datetime import date

print('===== EXERCÍCIO #101 =====')
print()

def votar(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos, não vota.\n'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos, o vota é opcional.\n'
    else:
        return f'Com {idade} anos, o vota é obrigatório.\n'


# Programa Principal
print('-' * 25)
data = int(input('Em que ano você nasceu? '))
print(votar(data))
