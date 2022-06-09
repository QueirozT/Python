from time import sleep


def linha(lenght=30):
    """
    Função que mostra uma linha
    - lenght: Tamanho da linha
    - return: Uma linha
    """
    print('-' * lenght)


def msg(txt):
    """
    Função que mostra uma mensagem formatada
    - txt: Texto a ser mostrado
    - return: Texto formatado
    """
    linha(50)
    print(txt.center(50))
    linha(50)


def palavraSecreta(palavra, dica):
    """
    Função que recebe uma palavra e uma dica e cria toda a lógica do jogo
    - palavra: Palavra secreta
    - dica: Dica para a palavra secreta
    - return: O jogo do adivinhação
    """
    palavraSecreta = list(palavra.upper())
    palpite = list('_' * len(palavraSecreta))
    letras = list()
    chances = 5

    while True:
        print(f'Palavra secreta: {"".join(palpite)}')
        print(f'Dica: {dica}')
        print()

        letra = input('Informe uma letra: ').strip().upper()[0]
        print()
        sleep(0.5)

        if letra in letras:
            msg('Você já informou essa letra!')
            print()
            sleep(1)
            continue
        letras.append(letra)
        
        for i, l in enumerate(palavraSecreta):
            if letra in l:
                palpite[i] = l
        
        if palpite == palavraSecreta:
            msg(f'Parabéns! A palavra era: {"".join(palavraSecreta)}')
            print()
            break
        elif letra in palavraSecreta:
            msg('Ótimo Palpite!')
            print()
            sleep(1)
        else:
            chances -= 1
            if chances > 0:
                msg(f'Você errou! Tentativas restantes: {chances}')
                print()
                sleep(1)
            else:
                msg(f'Tentativas restante: {chances} Você perdeu!')
                print()
                break
