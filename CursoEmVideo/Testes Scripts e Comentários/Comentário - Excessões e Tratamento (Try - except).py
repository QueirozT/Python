# EXCESSÕES: As excessões (Exception) são erros que podem acontecer a qualquer momento na execução do programa.

# As 'Exception' são erros que acontecem durante a execução do programa e podem ser tratadas.


# Como tratar uma excessão?
# ======================= #

# Para tratar uma excessão, utilizamos o bloco try/except.
# O bloco try é onde colocamos o código que queremos que seja executado.
# O bloco except é onde colocamos o código que será executado caso ocorra algum erro.
# EXEMPLO:
try:
    print(x)
except: # Tratando uma excessão genérica.
    print('Erro!')



# Como tratar uma excessão específica?
# ===================================== #

# Para tratar uma excessão específica, utilizamos o bloco try/except.
# O bloco try é onde colocamos o código que queremos que seja executado.
# O bloco except é onde colocamos o código que será executado caso ocorra algum erro.
# Dentro do except, podemos especificar qual excessão queremos tratar.
# EXEMPLO:
try:
    print(x)
except NameError: # Tratando uma excessão específica.
    print('Erro!')



# Como mostrar a mensagem de erro detalhada?
# ========================================= #

# Para mostrar a mensagem de erro detalhada, utilizamos o bloco try/except.
# O bloco try é onde colocamos o código que queremos que seja executado.
# O bloco except é onde colocamos o código que será executado caso ocorra algum erro.
# Dentro do except, podemos utilizar a palavra-chave Exception para capturar a excessão e mostrar a mensagem de erro detalhada.
# EXEMPLO:
try:
    print(x)
except Exception as erro: # Tratando a excessão e mostrando a mensagem de erro detalhada. 
    print(f'ERRO! {erro}')



# Como tratar múltiplas excessões?
# ============================== #

# Para tratar múltiplas excessões, utilizamos o bloco try/except.
# O bloco try é onde colocamos o código que queremos que seja executado.
# O bloco except é onde colocamos o código que será executado caso ocorra algum erro.
# Caso queira tratar mais de uma excessão, basta utilizar a palavra-chave 'except' múltiplas vezes detalhando as excessões.
# EXEMPLO:
try:
    print(x)
except NameError: # Tratando uma excessão específica
    print('Erro!')
except Exception as erro: # Tratando uma excessão genérica e mostrando a mensagem de erro detalhada
    print(f'ERRO! {erro}')
 
# ====================================================================================================================== #


# CAMPOS OPCIONAIS NO TRY/EXCEPT

# Além do bloco try/except, podemos utilizar o bloco try/except/else/finally.
# O bloco try é onde colocamos o código que queremos que seja executado.
# O bloco except é onde colocamos o código que será executado caso ocorra algum erro.
# O bloco else é onde colocamos o código que será executado caso não ocorra nenhum erro (OPCIONAL).
# O bloco finally é onde colocamos o código que será executado independente do resultado do bloco try/except (OPCIONAL).


# Utilizando o bloco try/except/else/finally
# ======================================== #

# Usando os blocos try/except/else/finally, podemos tratar erros de forma mais completa.
# Caso o bloco try não ocorra nenhum erro, o bloco else é executado, e caso ocorra, o bloco except é executado.
# Podemos utilizar mais de um bloco except para tratar múltiplas excessões.
# E o bloco finally é executado independente do resultado do bloco try/except/else, podendo ser utilizado para fechar conexões, etc. 
# EXEMPLO:
try:
    print(x)
except NameError:
    print('Erro!')
except Exception as erro:
    print(f'ERRO! {erro}') 
else:
    print('Não ocorreu nenhum erro!')
finally:
    print('Finalizando...')



# Tipos de erros e classes de erros:
# ================================ #

# Quando ocorre uma excessão, o Python Utiliza uma classe chamada Exception para representar o erro.
# Esta classe é uma classe genérica, que pode ser utilizada para representar qualquer erro.
# EXEMPLO:
try:
    print(x)
except Exception as erro: # Tratando uma excessão genérica e mostrando a mensagem de erro detalhada (o 'as' é para referenciar a excessão).
    print(f'ERRO! {erro}')



# Como ver o tipo de erro a partir da classe genéria Exception?
# =========================================================== #

# Para ver o tipo de erro a partir da classe genéria Exception, utilizamos o método '__class__'.
# Existem outros métodos para ver o tipo de erro ou outros detalhes, como '__name__' ou'__module__'.
# EXEMPLO:
try:
    print(x)
except Exception as erro: # Tratando uma excessão genérica e referenciando como 'erro'
    print(f'ERRO! {erro.__class__}') # Verificando o tipo de 'erro' através do método '__class__'.



# Uma lista de excessões Python pode ser encontrada em: https://docs.python.org/3/library/exceptions.html
# ====================================================================================================================== #
