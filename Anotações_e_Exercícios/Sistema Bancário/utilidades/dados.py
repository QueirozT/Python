"""
Módulo responsável pela formatação e entrada de dados do programa.

Este módulo contém uma função para validar a entrada de dados, para garantir que o usuário irá informar os valores corretamente. e para formatar a saída de dados.
"""

def msg(txt: str, tam: int=None, titulo: bool=False) -> None:
    """
    Função que exibe uma mensagem formatada na tela.

    Esta função recebe uma mensagem e a formata para ser exibida entre linhas. também recebe parâmetros opcionais para definir o tamanho das linhas ou remover uma das linhas.
        
        Parametros:
            txt (str):
                Texto a ser exibido.
            tam (int, None) - Opcional:
                Tamanho maximo das linhas no texto.
            titulo (bool) - Opcional: 
                True = exibe o texto como título (sem a linha de baixo).
        
        Retorno:
            None: A mensagem formatada será exibida no momento em que a função for chamada.
    """
    l = tam if tam else len(txt) + 10
    
    print("=" * l)
    print(f'{txt:^{l}}')
    print("=" * l) if not titulo else None


def leitura(txt: str, max: int=None) -> float:
    """
    Função que valida a entrada de dados.

    Esta função recebe uma mensagem que é exibida enquanto aguarda e valida a entrada de dados. após validar, retorna o valor validado. Ela também recebe um parâmetro opcional que informa o valor máximo que o usuário pode informar.

        Parametros:
            txt (str):
                Texto a ser exibido para o usuário.
            max (int, None) - Opcional:
                valor máximo aceitavel.
        
        Retorno:
            val (float): Valor válido digitado pelo usuário.
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
