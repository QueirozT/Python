print('===== EXERCÍCIO #103 =====')
print()


def jogador(n='<desconhecido>', g='0'):
    """
    -> Função para cadastrar dados de um jogador.
    :n = Nome do jogador.
    :g = Quantidade de gols feitos.
    :return: Print dos dados do jogador.
    # Criado por Tiago.
    """
    if not g.isnumeric():
        g = 0
    if len(n) == 0:
        n = '<desconhecido>'
    print(f'O jogador {n} fez {g} gols.')


# Programa Principal
nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ').strip()
jogador(nome, gols)
print()
