# Para quebrar linhas, use o \n em qualquer lugar do print()

# Para não quebrar linhas, use o end='' no final do print()


# Para delimitar o tamanho de um float, dentro das chaves de formatação utilize {:.2f}

# Para adicionar espaços extras contando a quantidade de caracteres da string, utilize {:^10}. para alinhar o texto a esquerda utilize {:<10} e para alinhar a direita utilize {:>10}. Para adicionar caracteres especiais, utilize {:=^10}

# EX:

altura = 1.7345
nome = 'Pedro'
peso = '60kg'

print(' O \n {:=^20} \n tem {:.2f} de altura e '.format(nome, altura), end='')

print('{}'.format(peso))


