from formula import *

print('Validador de CPF')
print()

cpf = cpf('Informe o CPF: ')
print()

print('Primeira função para validar um cpf:')
msg(f'O CPF informado é {"Válido" if validarCPF(cpf) else "Inválido"}')
print()

print('Segunda função para validar um cpf:')
msg(f'O CPF informado é {"Válido" if validadorAlternativo(cpf) else "Inválido"}')
print()
