def leiaDinheiro(txt):
    while True:
        valor = str(input(txt)).replace(',','.').strip()

        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO! "{valor}" não é um preço válido. Tente novamente.\033[m')
        else:
            return float(valor)
            break
