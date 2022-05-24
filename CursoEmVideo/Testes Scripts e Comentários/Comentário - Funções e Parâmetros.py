# FUNÇÕES: O Python é repleto de Rotinas, as famosas (FUNÇÕES).

# Funções ou Rotinas, são comandos pré definidos para executar ações. No python, as funções são definidas com o comando def.
# Após criar uma definição de função, é possível chamar a função através do nome da função.
# Sempre que criar uma def, deve dar duas linhas de espaço para manter o código limpo.

#  Como criar uma função?
# Para criar uma função, é só utilizar o comando Def e o nome da função(): e após a quebra de linha, colocar o código executado.
# EXEMPLO: Criando uma função para mostrar uma linha.
def lin():
    print('-' * 40)


#  Como chamar uma função?
# Para chamar ou executar uma rotina (FUNÇÃO), é só utilizar o nome da função.
# EXEMPLO: Chamando a função lin() para mostrar uma linha.
lin()

#=======================================================================================================================


# PARÂMETROS: Parâmetros são variáveis que são passadas para uma função.

# Os parâmetros de uma função são definidos entre os parênteses() da função, e servem para passar dados para a função.
# Parâmetros podem ser valores que serão aprsentados na chamada da função, ou podem ser variáveis que serão definidas dentro da função.
# Os parâmetros também podem receber valores padrões que serão utilizados caso nenhum valor seja passado na chamada da função.

# Como definir um parâmetro?
# Para definir um parâmetro, é só colocar o nome da variável entre os parênteses() da função.
# EXEMPLO: Definindo um parâmetro de tamanho para a função lin().
def lin(tam=40):
    print('-' * tam)


# Como chamar uma função com parâmetros?
# Para chamar uma função com parâmetros, é só colocar os valores dos parâmetros entre os parênteses() da função.
# EXEMPLO: Chamando a função lin() com o parâmetro de tamanho 30.
lin(30)
