import cpf

print('Validador de CPF')
print()

cpf_val = cpf.recebe_cpf('Informe o CPF: ')
print()

print('Primeira função para validar um cpf:')
cpf.msg(f'O CPF informado é {"Válido" if cpf.validarCPF(cpf_val) else "Inválido"}')
print()

print('Segunda função para validar um cpf:')
cpf.msg(f'O CPF informado é {"Válido" if cpf.validadorAlternativo(cpf_val) else "Inválido"}')
print()
