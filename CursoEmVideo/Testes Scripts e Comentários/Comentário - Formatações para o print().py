altura = 1.7345 # O valor em ponto flutuante será delimitado pela formatação {:.2f}

nome = 'Pedro' # O nome receberá espaços extras caso a quantidade de caracteres seja menor que a da formatação {:^20} e receberá '=' para preecher os espaços vazios.

peso = '60kg'

print('O {:=^20} tem {:.2f} e '.format(nome, altura), end='') # O próximo print() será concatenado ao final graças ao end='' que remove quebras de linha.

print('{}'.format(peso))
