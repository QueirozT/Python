print('===== EXERCÍCIO #096 =====')
print()

def msg(text): # Definindo uma função de formatação com um parâmetro texto.
    print('-' * (len(text) + 10))
    print(f'{text:^{len(text) + 10}}') # Para calcular um valor dentro das chaves é só colocar os valores dentro de outras chaves.
    print('-' * (len(text) + 10))


def area(l=0, c=0): # Definindo uma função de cálculo de área com dois parâmetros.
    return l * c


msg('Controle de Terrenos') # Chamando a função msg() com o texto dentro do parâmetro.
print()

larg = float(input('Qual a largura? '))
comp = float(input('Qual o comprimento? '))
print()

# Chamando uma função com F-Strings dentro de outra função.
msg(f'A área de um terreno {larg:.1f} x {comp:.1f} é de {area(larg, comp):.1f}m².')
print()
