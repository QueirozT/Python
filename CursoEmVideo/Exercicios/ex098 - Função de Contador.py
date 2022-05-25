from time import sleep # Para usar a função sleep em loops, é necessário habilitar o flush do print.

print('===== EXERCÍCIO #098 =====')
print()

def contador(ini=0, fim=0, pas=0):
    print('=' * 30)
    print(f'Contando de {ini} até {fim} de {pas} em {pas}')
    sleep(2.5)

    if ini < fim:
        if pas < 0:
            pas = pas * -1 # Se o passo for negativo, inverte o valor.
        for i in range(ini, fim, pas):
            print(i, end=' ', flush=True) # Ativando o flush para que o print seja exibido imediatamente.
            sleep(0.5)
        print('FIM!') 
    elif ini > fim:
        if pas > 0:
            pas = pas * -1 # Se o passo for positivo, inverte o valor.
        for i in range(ini, fim, pas):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        print('Não é possível contar.')
    print()


# Programa Principal.
contador(1, 10, 1)

contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print()

contador(i, f, p)
