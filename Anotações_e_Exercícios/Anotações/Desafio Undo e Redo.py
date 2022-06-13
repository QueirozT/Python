"""
Este programa é a solução de um desafio que consiste em receber valores, armazenar, manipular e retornar os valores armazenados.
Ações:
- Adicionar valores.
- Imprimir os valores.
- Desfazer.
- Refazer.
"""


def show(list):
    """
    Função que imprime os valores armazenados em uma lista.
    - list: Lista que será impressa.
    """
    if not list:
        print('\nTarefas: \n-')
    else:    
        print(f'\nTarefas:')
        for i in list:
            print(f'- {i}')


def undo_tarefa(list, redo_list):
    """
    Função que desfaz a última ação realizada.
    - list: Lista que será desfeita.
    - redo_list: Lista que armazena os valores desfeitos.
    """
    if not list:
        print('Nenhuma tarefa para desfazer.')
    else:
        redo_list.append(list.pop())
        print('Desfazendo...')


def redo_tarefa(list, redo_list):
    """
    Função que refaz a última ação desfeita.
    - list: Lista que será refeita.
    - redo_list: Lista que armazena os valores refeitos.
    """
    if not redo_list:
        print('Nenhuma tarefa para refazer.')
    else:
        list.append(redo_list.pop())
        print('Refazendo...')


if __name__ == '__main__':
    from time import sleep

    tarefas = []
    redo = []

    while True:
        show(tarefas)

        opcao = input('\n[undo, redo, sair] - Qual a nova tarefa? ').strip().capitalize()
        sleep(1)
        
        if opcao.upper() == 'SAIR':
            print('Finalizando...\n')
            sleep(1)
            break
        
        if opcao.upper() == 'UNDO':
            undo_tarefa(tarefas, redo)
            sleep(1)
            continue
        
        if opcao.upper() == 'REDO':
            redo_tarefa(tarefas, redo)
            sleep(1)
            continue
        
        tarefas.append(opcao)
        redo.clear()



# VERSÃO ANTIGA
# from time import sleep

# tarefas = []
# redo = []

# while True:
#     print(f'\n{"-" * 30}\n{"Lista de Tarefas":^30}\n{"-" * 30}')
#     print(f'1 - Nova Tarefa\n2 - Visualizar Tarefas\n3 - Desfazer\n4 - Refazer\n5 - Sair')
    
#     try:
#         opcao = int(input('Digite a opção desejada: ')[0])
#         if opcao < 1 or opcao > 5:
#             raise ValueError
        
#         if opcao == 5:
#             print('\nSaindo do programa...\n')
#             break
#     except:
#         print('\nOpção inválida!')
#         sleep(1)
#         continue

#     if opcao == 1:
#         tarefa = input('\nQual a nova tarefa? ').strip().capitalize()
#         tarefas.append(tarefa)
#         redo.clear()
#         print('Tarefa adicionada com sucesso!')
#         sleep(1)
#         continue
    
#     if opcao == 2:
#         if not tarefas:
#             print('\nNão há tarefas cadastradas!')
#             sleep(1)
#             continue
#         print(f'\n{" Tarefas ":=^30}')
#         for i, t in enumerate(tarefas):
#             print(f'{i + 1}°: {t}')
#         print("=" * 30)
#         sleep(len(tarefas))
#         continue

#     if opcao == 3:
#         if not tarefas:
#             print('\nNão há tarefas para desfazer!')
#             sleep(1)
#             continue
#         redo.append(tarefas[-1])
#         tarefas.pop()
#         print(f'\nTarefa desfeita com sucesso!')
#         sleep(1)
#         continue

#     if opcao == 4:
#         if not redo:
#             print('\nNão há tarefas para refazer!')
#             sleep(1)
#             continue
#         tarefas.append(redo[-1])
#         redo.pop()
#         print(f'\nTarefa refeita com sucesso!')
#         sleep(1)
