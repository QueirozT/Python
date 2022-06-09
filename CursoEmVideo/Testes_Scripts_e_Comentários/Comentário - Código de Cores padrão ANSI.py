# Para usar o código de cores sem fazer importação, basta utilizar o padrão "ANSI" que é suportado pelo python: https://docs.python.org/3/library/colorsys.html

# para formatar o código de cores ANSI, basta utilizar o padrão: \033[<cor>;<estilo>;<tamanho>m
# para limpar a formatação de cores, basta utilizar o padrão: \033[0;0;0m ou \033[0m

# Ex: 
print('\033[6;30;41mOlá, mundo!\033[m')

print('Olá, {}este é um teste de cores{}...'.format('\033[4;34m','\033[m'))


# ESTILOS:
# 0 - Sem estilo
# 1 - Negrito
# 4 - Sublinhado
# 7 - Invertido (Inverte cor de fundo e texto)

# CORES:
# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Roxo
# 36 - Ciano
# 37 - Cinza

# FONTE:
# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Roxo
# 46 - Ciano
# 47 - Cinza

# Outros estilos e cores podem ser encontrados através de bibliotecas como: https://docs.python.org/3/library/colorsys.html	