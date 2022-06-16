"""
Este programa é a solução para um desafio que consiste em utilizar POO para criar um sistema de contas bancárias.
Estou utilizando o conceito de herança e polimorfismo para criar classes que representam contas bancárias.
Também estou criando um módulo que simula um banco de dados e um módulo para as funções de formatação e tratamento de dados.
"""
from Contas.cc import ContaCorrente
from Contas.cp import ContaPoupanca
from Contas import BancoDeDados as bd
from Contas import uteis
from time import sleep

# Programa Principal
while True:
    uteis.msg("BANCO DINDIN PRA MIM", titulo=True)
    uteis.msg(f"Opções: \n1 - Criar uma conta \n2 - Entrar em uma conta \n3 - Apagar uma conta \n4 - Sair", 30)
    
    op = uteis.leitura("\nOpção: ", 4)
    print()

    # Criando uma conta
    if op == 1:
        while True:
            uteis.msg("CRIAR UMA CONTA", titulo=True)
            uteis.msg(f"Opções: \n1 - Conta Corrente \n2 - Conta Poupança \n3 - Voltar", 25)
            
            op = uteis.leitura("\nOpção: ", 3)
            print()

            if op == 1:
                uteis.msg("CRIANDO CONTA CORRENTE")
                a = input('Agência: ')
                c = input('Conta: ')
                bd.atualizar(agencia=a, conta=c, saldo=0, limite=200)
                continue
            if op == 2:
                uteis.msg("CRIANDO CONTA POUPANÇA")
                a = input('Agência: ')
                c = input('Conta: ')
                bd.atualizar(agencia=a, conta=c, saldo=0)
                continue
            if op == 3:
                uteis.msg("VOLTANDO...")
                sleep(1)
                op = None
                break

    # Entrando em uma conta
    if op == 2:
        uteis.msg('ENTRANDO NA CONTA')
        agencia = input('Agência: ')
        conta = input('Conta: ')

        if bd.buscar(agencia, conta):
            uteis.msg('CONTA ENCONTRADA')
            sleep(1)
            
            conta = bd.buscar(agencia, conta)

            if conta.get('ContaCorrente'):
                conta = ContaCorrente(conta['agencia'], conta['conta'], conta['saldo'], conta['ContaCorrente']['limite'])
                tipo = 'CC'
            elif conta.get('ContaPoupanca'):
                conta = ContaPoupanca(conta['agencia'], conta['conta'], conta['saldo'])
                tipo = 'CP'
            
            while True:
                uteis.msg(f"AG: {conta.agencia} {tipo}: {conta.conta}", 30, titulo=True)
                uteis.msg(f"Opções: \n1 - Saldo \n2 - Depositar \n3 - Sacar \n4 - voltar", 30)
            
                op = uteis.leitura("\nOpção: ", 4)
                print()

                if op == 1:
                    uteis.msg(f"Saldo: R${conta.saldo:.2f}")
                    sleep(1)
                if op == 2:
                    valor = uteis.leitura("Quanto deseja depositar? ")
                    conta.depositar(valor)
                    uteis.msg("Depositando...")
                    sleep(1)
                if op == 3:
                    while True:
                        try:
                            valor = float(uteis.leitura("Quanto deseja sacar? "))
                            conta.sacar(valor)
                        except ValueError as e:
                            print(e)
                        else:
                            uteis.msg("Sacando...")
                            sleep(1)
                            break
                if op == 4:
                    if tipo == 'CC':
                        bd.atualizar(conta.agencia, conta.conta, conta.saldo, conta.limite)
                    elif tipo == 'CP':
                        bd.atualizar(conta.agencia, conta.conta, conta.saldo)
                    
                    uteis.msg("VOLTANDO...")
                    sleep(1)
                    op = None
                    break
        else:
            uteis.msg('CONTA NÃO ENCONTRADA')
            sleep(1)
            continue

    # Apagando uma conta
    if op == 3:
        while True:
            uteis.msg("APAGAR UMA CONTA", titulo=True)
            uteis.msg(f"Opções: \n1 - Listar as Contas \n2 - Apagar \n3 - Voltar", 26)
            
            op = uteis.leitura("\nOpção: ", 3)
            print()

            if op == 1:
                uteis.msg("LISTA DE AGÊNCIAS / CONTAS")
                bd.listar()
                print()
                sleep(1)
            if op == 2:
                uteis.msg("APAGANDO A CONTA")
                agencia = input('Agência: ')
                conta = input('Conta: ')
                bd.remover(agencia, conta)
                print()
                sleep(1)
            if op == 3:
                uteis.msg("VOLTANDO...")
                print()
                sleep(1)
                op = None
                break
    if op == 4:
        uteis.msg('Finalizando o programa...')
        print()
        break
