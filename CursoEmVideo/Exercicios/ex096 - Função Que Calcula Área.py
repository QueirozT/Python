print('===== EXERCÍCIO #096 =====')
print()

def msg(text): # Definindo uma função de formatação com um parâmetro texto.
    print('-' * (len(text) + 10))
    print(f'{text:^{len(text) + 10}}') # Para calcular um valor dentro das chaves é só colocar os valores dentro de outras chaves.
    print('-' * (len(text) + 10))


def area(a=0, b=0): # Definindo uma função de cálculo de área com dois parâmetros.
    return a * b


msg('Controle de Terrenos') # Chamando a função msg() com o texto dentro do parâmetro.
print()

largura = float(input('Qual a largura? '))
altura = float(input('Qual a altura? '))
print()

# Chamando uma função com F-Strings dentro de outra função.
msg(f'A área de um terreno {largura:.1f} x {altura:.1f} é de {area(largura, altura):.1f} m².')
print()
