"""
Desafio POO - Sistema Bancário (Extremamente Simples)

Este programa é a solução para um desafio que consiste em utilizar POO para criar um sistema de contas bancárias.
Estou utilizando classes, um módulo que simula um banco de dados e um módulo para as funções de formatação e tratamento de dados.
"""
from utilidades.classes.cc import ContaCorrente
from utilidades.classes.cp import ContaPoupanca
from utilidades import BancoDeDados as bd
from utilidades.dados import msg, leitura
from time import sleep

# Programa Principal
while True:
    msg("BANCO DINDIN PRA MIM", titulo=True)
    msg(f"Opções: \n1 - Criar uma conta \n2 - Entrar em uma conta \n3 - Apagar uma conta \n4 - Sair", 30)
    
    op = leitura("\nOpção: ", 4)
    print()

    # Criando uma conta
    if op == 1:
        while True:
            msg("CRIAR UMA CONTA", titulo=True)
            msg(f"Opções: \n1 - Conta Corrente \n2 - Conta Poupança \n3 - Voltar", 25)
            
            op = leitura("\nOpção: ", 3)
            print()

            if op == 1:
                msg("CRIANDO CONTA CORRENTE")
                a = input('Agência: ')
                c = input('Conta: ')
                bd.atualizar(agencia=a, conta=c, saldo=0, limite=200)
                continue
            if op == 2:
                msg("CRIANDO CONTA POUPANÇA")
                a = input('Agência: ')
                c = input('Conta: ')
                bd.atualizar(agencia=a, conta=c, saldo=0)
                continue
            if op == 3:
                msg("VOLTANDO...")
                sleep(1)
                op = None
                break

    # Entrando em uma conta
    if op == 2:
        msg('ENTRANDO NA CONTA')
        agencia = input('Agência: ')
        conta = input('Conta: ')

        if bd.buscar(agencia, conta):
            msg('CONTA ENCONTRADA')
            sleep(1)
            
            conta = bd.buscar(agencia, conta)

            if conta.get('ContaCorrente'):
                conta = ContaCorrente(conta['agencia'], conta['conta'], conta['saldo'], conta['ContaCorrente']['limite'])
                tipo = 'CC'
            elif conta.get('ContaPoupanca'):
                conta = ContaPoupanca(conta['agencia'], conta['conta'], conta['saldo'])
                tipo = 'CP'
            
            while True:
                msg(f"AG: {conta.agencia} {tipo}: {conta.conta}", 30, titulo=True)
                msg(f"Opções: \n1 - Saldo \n2 - Depositar \n3 - Sacar \n4 - voltar", 30)
            
                op = leitura("\nOpção: ", 4)
                print()

                if op == 1:
                    msg(f"Saldo: R${conta.saldo:.2f}")
                    sleep(1)
                if op == 2:
                    valor = leitura("Quanto deseja depositar? ")
                    conta.depositar(valor)
                    msg("Depositando...")
                    sleep(1)
                if op == 3:
                    while True:
                        try:
                            valor = leitura("Quanto deseja sacar? ")
                            conta.sacar(valor)
                        except ValueError as e:
                            print(e)
                        else:
                            msg("Sacando...")
                            sleep(1)
                            break
                if op == 4:
                    if tipo == 'CC':
                        bd.atualizar(conta.agencia, conta.conta, conta.saldo, conta.limite)
                    elif tipo == 'CP':
                        bd.atualizar(conta.agencia, conta.conta, conta.saldo)
                    
                    msg("VOLTANDO...")
                    sleep(1)
                    op = None
                    break
        else:
            msg('CONTA NÃO ENCONTRADA')
            sleep(1)
            continue

    # Apagando uma conta
    if op == 3:
        while True:
            msg("APAGAR UMA CONTA", titulo=True)
            msg(f"Opções: \n1 - Listar as Contas \n2 - Apagar \n3 - Voltar", 26)
            
            op = leitura("\nOpção: ", 3)
            print()

            if op == 1:
                msg("LISTA DE AGÊNCIAS / CONTAS")
                bd.listar()
                print()
                sleep(1)
            if op == 2:
                msg("APAGANDO A CONTA")
                agencia = input('Agência: ')
                conta = input('Conta: ')
                bd.remover(agencia, conta)
                print()
                sleep(1)
            if op == 3:
                msg("VOLTANDO...")
                print()
                sleep(1)
                op = None
                break
    if op == 4:
        msg('Finalizando o programa...')
        print()
        break
