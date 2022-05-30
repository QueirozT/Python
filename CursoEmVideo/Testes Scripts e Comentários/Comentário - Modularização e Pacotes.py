# MODULARIZAÇÃO: É uma forma de organizar um programa, de forma que ele possa ser reutilizado em outros programas.

# Todos arquivos .py que contiverem uma função podem ser importados para outros programas.


# Como modularizar um programa?
# =========================== #

# Os passos para criar um módulo são:
# 1 - Criar um arquivo de funções.
# 2 - Importar o arquivo de funções no programa principal.
# 3 - Chamar o import quando for utilizar as funções.



# Como inportar um módulo?
# ==================== #

# Para chamar um módulo, basta utilizar o nome do módulo.
# EX: import modulo
#     modulo.funcao()



# Quais as vantagens de modularizar um programa?
# ============================================ #

# 1 - Reduz o código / Organiza.
# 2 - Melhorar a legibilidade do código.
# 3 - Facilita a manutenção do código.
# 4 - Ocultar detalhes do programa.
# 5 - Reutilização de código.

# ====================================================================================================================== #

# PACOTES OU BIBLIOTECAS: É um conjunto de módulos.

# Os pacotes ou Bibliotecas são mais uma forma de organizar o programa, separando os módulos em pastas.


# Como criar um pacote?
# =================== #

# Para criar um pacote, basta criar uma pasta com o nome do pacote e um arquivo __init__.py com os códigos dos módulos.
# Ou sub-pacotes, cada um com o seu arquivo __init__.py com as suas funções dentro.
# EX:
# Pasta: pacote
#       Arquivo: __init__.py
#       Sub-Pasta: numeros
#           Arquivo: __init__.py
#       Sub-Pasta: strings
#           Arquivo: __init__.py



# Como importar um Pacote/Biblioteca?
# ================================= #

# Importar um pacote é o mesmo que importar um módulo.
# Porém, se ele contiver sub-pacotes, precisa utilizar o nome de cada sub-pacote na chamada da função.
# EX: 
# import pacote
# pacote.numeros.função()


# Uma forma de reduzir o código na importação de pacotes com sub-pacotes como no exemplo criado a cima,
# É chamando o módulo / sub-pacote específico do pacote principal.
# EX:
# from pacote import numeros
# numeros.função()
