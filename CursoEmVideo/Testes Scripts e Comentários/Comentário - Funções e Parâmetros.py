# FUNÇÕES: O Python é repleto de Rotinas, as famosas (FUNÇÕES).

# Funções ou Rotinas, são comandos pré definidos para executar ações. No python, as funções são definidas com o comando def.
# Após criar uma definição de função, é possível chamar a função através do nome da função.
# Sempre que criar uma def, deve dar duas linhas de espaço para manter o código limpo.


#  Como criar uma função?
# ===================== #

# Para criar uma função, é só utilizar o comando Def e o nome da função(): e após a quebra de linha, colocar o código executado.
# EXEMPLO: Criando uma função para mostrar uma linha.
def lin():
    print('-' * 40)


# Como chamar uma função?
# ====================== #

# Para chamar ou executar uma rotina (FUNÇÃO), é só utilizar o nome da função.
# EXEMPLO: Chamando a função lin() para mostrar uma linha.
print('EX 01 - Chamando uma função simpels.')
lin()

#=======================================================================================================================



# PARÂMETROS: Parâmetros são variáveis que são passadas para uma função.

# Os parâmetros de uma função são definidos entre os parênteses() da função, e servem para passar dados para a função.
# Parâmetros podem ser valores que serão aprsentados na chamada da função, ou podem ser variáveis que serão definidas dentro da função.
# Os parâmetros também podem receber valores padrões que serão utilizados caso nenhum valor seja passado na chamada da função.


# Como definir um parâmetro?
# ======================== #

# Para definir um parâmetro, é só colocar o nome da variável, ou os nomes das variáveis entre os parênteses() da função.
# EXEMPLO: Definindo um parâmetro com uma mensagem para ser exibida formatada.
def msg(text):
    print('-' * (len(text) + 10))
    print(f'{text:^{len(text) + 10}}')
    print('-' * (len(text) + 10))



# Como chamar uma função com parâmetros?
# Para chamar uma função com parâmetros, é só colocar os valores dos parâmetros entre os parênteses() da função.
# EXEMPLO: Chamando a função msg() com o texto dentro do parâmetro.
print('\n EX 02 - Chamando uma função com parâmetros.')
msg('Mensagem de Teste!')



# É possível definir mais de um parâmetro.
#======================================= #
 
# EXEMPLO: Definindo dois parâmetros para uma função de soma.
def soma(a, b):
    print(a + b)


# Como chamar uma função com mais de um parâmetro?
# Para chamar uma função com mais de um parâmetro, é só colocar os valores dos parâmetros entre os parênteses() da função.
# EXEMPLO: Chamando a função soma() com os valores dentro dos parâmetros.
print('\n EX 03 - Chamando uma função com mais de um parâmetro.')
soma(10, 20)



# Retornando o resultado de uma série de operações.
# =============================================== #

# É possível também criar uma função com muitos comandos e retornar apenas um valor.
# EXEMPLO: Definindo uma função que retorna o valor do fatorial(!) de um número.
def fat(num):
    ant = num
    res = 0
    
    for i in range(num):
        ant -= 1
        res += num * ant
        num = ant
    
    return res


# Como chamar uma função que retorna um valor?
# EXEMPLO: Chamando a função fat() com o valor que será calculado dentro do parâmetro e exibindo o resultado.
print('\n EX 04 - Chamando uma função que retorna o resultado de operações.')
print('O fatorial de 4 é: ', fat(4))



# Passando F-Strings e outras funções dentro de uma função com formatação de texto.
# =============================================================================== #

# Passando um valor com F-String (Formatação de Strings) para uma função com outra F-String.
# EXEMPLO: Re-utilizando a função msg() que exibe uma mensagem formatada e passando uma mensagem com F-String como parâmetro.
print('\n EX 05 - Chamando uma função com F-Strings e outras funções.')
msg(f'Fim do Programa! Fatorial de 5 é: {fat(5)} e Fatorial de 10 é: {f"{fat(10)}"}')

#=======================================================================================================================



# Utilizando um "Empacotador" para receber vários parâmetros de uma função.
# ======================================================================= #

# Uma função com um parâmetro empacotador retorna uma tupla com os valores passados.
# Para utilizar um empacotador, é só declarar a função com um * seguido da variável no parâmetro. def contador(* variavel)
# EXEMPLO: Definindo uma função contador que recebe vários parâmetros.
def contador(* num):
    print(f'Foram passados {len(num)} valores para o contador.')
    print(f'Os valores foram: {num}')


# Como chamar uma função com um parâmetro empacotador?
# EXEMPLO: Chamando a função contador() com os valores que serão passados dentro do parâmetro.
print('\n EX 06 - Chamando uma função com um parâmetro empacotador.')
contador(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



# Utilizando Listas como parâmetros.
# ================================ #

# Para utilizar listas, não precisa declarar a função com um * seguido da variável, basta utilizar a lista entre os parênteses() da função.
# EXEMPLO: Definindo uma função que recebe uma lista como parâmetro.
def lista(l):
    print(f'A lista tem {len(l)} elementos.')
    print(f'Os valores da lista são: {l}')



# Como chamar uma função com uma lista como parâmetro?
# Posso criar uma lista e passar o nome da variável ou declarar uma lista dentro de parênteses() da função.
# EXEMPLO: Chamando a função lista() com a lista que será passada dentro do parâmetro.
print('\n EX 07 - Chamando uma função com uma lista como parâmetro.')
lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



# Parâmetros opcionais.
# =================== #

# Os parâmetros opcionais são os parâmetros que não são obrigatórios e que mesmo que não sejam passados, o programa irá executar a função.
# Para definir um parâmetro opcional, é só colocar um = no final do parâmetro.
# EXEMPLO: Definindo uma função que recebe um parâmetro opcional.
def opcional(nome, sobrenome=''):
    """
    -> Esta função recebe um parâmetro opcional.
    :param nome: O primeiro parâmetro é obrigatório.
    :param sobrenome: O segundo parâmetro é opcional.
    :return: Não retorna nada.
    """
    print(f'Olá {nome} {sobrenome}!')


# Como chamar uma função com um parâmetro opcional?
# EXEMPLO: Chamando a função opcional() com os valores que serão passados dentro dos parâmetros.
print('\n EX 08 - Chamando uma função com um parâmetro opcional.')
opcional('João')
print('Com o parâmetro opcional fica: ')
opcional("João", "Silva")
