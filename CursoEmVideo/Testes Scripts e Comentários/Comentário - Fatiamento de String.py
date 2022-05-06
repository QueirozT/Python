# FATIAMENTO DE STRING
#=====================#

# Para fatiar uma string, basta chamar a variável e colocar o símbolo [].

# Exemplo: nome = 'José' print(nome[0]) -> imprime 'J', ou seja, o primeiro caractere da string.

# Exemplo: nome = 'José' print(nome[-1]) -> imprime 'é', ou seja, o último caractere.


# Exemplo: nome = 'José' print(nome[1:4]) -> imprime 'osé', ou seja, os caracteres de 1 a 3 pois o último sempre é ignorado.

# Exemplo: nome = 'José' print(nome[0:-1:2]) -> imprime 'Js', ou seja, o primeiro e o terceiro caractere, pois vai pular de 2 em 2.

# Exemplo: nome = 'Jose' print(nome[0::2]) -> imprime 'Js' ou seja, o primeiro e o terceiro caractere, pois vai pular de 2 em 2 até o fim.


# Exemplo: nome = 'José' print(nome[:2]) -> imprime 'Jo', ou seja, vai exibir todos os valores anteriores ao inforado.

# Exemplo: nome = 'José' print(nome[2:]) -> imprime 'se', ou seja, todos os caracteres a partir do 2 incluindo ele mesmo.


# Exemplo: nome = 'José' print(nome[:-1]) -> imprime 'Jos', ou seja, os caracteres a partir do último caractere, exceto o último.

# Exemplo: nome = 'José' print(nome[::-1]) -> imprime 'ésoJ', ou seja, os caracteres a partir do último caractere, em ordem reversa.



# ANÁLISE DE STRING
#==================#

frase = 'Curso em Video de Python'

len(frase) # Retorna o tamanho da string.

'curso' in frase # O 'in' Retorna True ou False, ou seja, existe esta string dentro da variável frase.

frase.count('o') # Retorna a quantidade de ocorrências de 'o' na string.
frase.count('o', 0, 13) # Retorna a quantidade de ocorrências de 'o' na string, entre os índices 0 e 13.

frase.find('deo') # Retorna o índice da primeira ocorrência de 'deo' na string.
frase.rfind('deo') # O .rfind() é o mesmo que o .find(), porém, começa a busca do último caractere, mostrando o índice do último caractere.
frase.find('Android') # Retorna -1, ou seja, não encontrou.



# TRANSFORMAÇÃO DE STRING
#========================#

frase.replace('Python', 'Android') # Substitui todas as ocorrências de 'Python' por 'Android'.

frase.upper() # Converte todas as letras para maiúsculas.
frase.lower() # Converte todas as letras para minúsculas.

frase.capitalize() # Converte a primeira letra da frase para maiúscula e o resto para minuscula.
frase.title() # Converte todas as letras para minusculas, exceto as primeiras letras de cada palavra.

frase.strip() # Remove os espaços em branco no início e no fim da string.
frase.rstrip() # Remove os espaços em branco no final da string.
frase.lstrip() # Remove os espaços em branco no início da string.



# DIVISÃO DE STRING
#==================#

frase.split() # Divide a string em uma lista, onde cada elemento é uma palavra.



# JUNÇÃO DE STRING
#==================#

'-'.join(frase) # Junta todas as palavras da string, separadas por um traço. ps: Pode substituir o "-" por qualquer coisa, até mesmo espaço.
