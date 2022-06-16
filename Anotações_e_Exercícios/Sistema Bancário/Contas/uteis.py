def msg(txt, tam=None, titulo=False):
    """
    Função que exibe uma mensagem formatada na tela.
    - txt: Texto a ser exibido.
    - tam: (Opcional) Tamanho maximo das linhas no texto.
    - titulo: (Opcional) Se True, exibe o texto como título, sem as linhas de baixo.
    """
    l = tam if tam else len(txt) + 10
    
    print("=" * l)
    print(f'{txt:^{l}}')
    print("=" * l) if not titulo else None


def leitura(txt, max=None):
    """
    Função que valida a entrada de dados.
    - txt: Texto a ser exibido para o usuário.
    - max: (Opcional) valor máximo aceitavel.
    - return: Valor digitado pelo usuário.
    """
    while True:
        try:
            val = round(float(input(txt).replace(',', '.')), 2)  # Converte o valor para float e arredonda para duas casas decimais.
            if max:
                if val > max or val < 1:
                    raise
        except:
            print("Opção inválida")
            continue
        else:
            return val
