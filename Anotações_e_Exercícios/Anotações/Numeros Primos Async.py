"""
Calculando números primos de forma assíncrona.

Este é um exemplo de como o módulo asyncio funciona.
Neste script, é utilizado o módulo asyncio para criar uma função assíncrona que recebe um número e retorna o maior número primo menor que o número passado.
O módulo asyncio é um módulo que permite a criação e gerenciamento de funções assíncronas, ou seja, que não necessariamente precisam ser executadas na ordem em que foram criadas.


Como a chamada de uma função assíncrona é feita de forma assíncrona, o resultado da função é impresso de forma assincrona.
    Resultado esperado:
        Maior primo até 2
        Maior primo: 1
        Maior primo até 10000
        Maior primo até 1000
        Maior primo até 100
        Maior primo: 997
        Maior primo: 97
        Maior primo: 9973
        Levou 390.96 ms
"""
import asyncio
import time


def primo(n: int) -> bool:
    """
    Esta função verifica se um número é primo.

    Esta função executa uma verificação de primalidade para um número.
    Se o resultado da divisão inteira do número for igual ao resultado da divisão real por qualquer número maior que 1 e menor que o número, então o número não é primo.

    :param n: número a ser verificado
    :return: True se o número for primo, False caso contrário
    """
    return not any(n//i == n/i for i in range(n-1, 1, -1))


async def maior_primo_menor_que(n: int) -> None:
    """
    Encontra o maior número primo menor que o número informado.

    Esta função encontra o maior número primo menor que o número informado e imprime o resultado.
    Ela utiliza o módulo asyncio, permitindo que a função seja executada de forma assíncrona multiplas vezes.
    
    :param n: número a ser verificado
    :return: None
    """
    print(f'Maior primo até {n}')
    for val in range(n-1, 0, -1):
        if primo(val):
            print(f'Maior primo: {val}')
            return val
        await asyncio.sleep(0.01)  # Criando um await (aguardável) permitindo que a função seja executada de forma assíncrona.


async def main():
    """
    Chama a função maior_primo_menor_que.

    Esta função chama a função maior_primo_menor_que multiplas vezes através do agregador de corotinas asyncio.gather(), 
    e contabiliza o tempo de execução. Gracas ao gather que agrega todas as chamadas, elas são executada de forma concorrente assincrona, então os resultados são impressos de forma assincrona.

    :return: None
    """
    t0 = time.time()
    await asyncio.gather(
        maior_primo_menor_que(2),
        maior_primo_menor_que(10000),
        maior_primo_menor_que(1000),
        maior_primo_menor_que(100)
    )
    t1 = time.time()
    print(f'Levou {1000*(t1-t0):.2f} ms')


# Executando a função main com o módulo asyncio para que a função seja executada de forma assíncrona.
asyncio.run(main())
