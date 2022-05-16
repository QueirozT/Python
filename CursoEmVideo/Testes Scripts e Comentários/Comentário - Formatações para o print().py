# Para quebrar linhas, use o \n em qualquer lugar do print()

# Para não quebrar linhas, use o end='' no final do print()

# Para delimitar o tamanho de um float, dentro das chaves de formatação utilize {:.2f}


# Para mostrar tudo exatamente como está sendo digitado até com quebra de linha, use áspas triplas dentro do print(''' texto ''').
# EX:

print(''' 
Exemplo de frase
com quebra
de linha 
''')


# Para adicionar espaços extras contando a quantidade de caracteres da string, utilize {:^10}. para alinhar o texto a esquerda utilize {:<10} e para alinhar a direita utilize {:>10}. Para adicionar caracteres especiais, utilize {:=^10}
# EX:

altura = 1.7345
nome = 'Pedro'
peso = '60kg'

print(' O \n {:=^20} \n tem {:.2f} de altura e '.format(nome, altura), end='')

print('{}'.format(peso))



# O .format() serve para formatar uma "{}" dentro de um texto, e pode ser usado quantas vezes quiser contanto que esteja logo após o 'texto'.
# EX:

nome = 'pedro'
idade = 20
altura = 1.73

print('{:^60}'.format('O {} tem {} anos e {}m de altura'.format(nome, idade, altura))) # Alinhei o texto ao centro de 60 caracteres.



# Através das '{}' posso definir o ponto flutuante do numero que será exibido, mas também posso definir o formato de exibição do numero.
# EX:

print('{:<3.2f}'.format(altura)) # Alinhei o texto a esquerda em um espaço de até 3 digitos e com 2 casas decimais.



# Pode utilizar condicionais dentro do format()
# EX:

n = 3
print(' + ' if n != 0 else ' = ')
