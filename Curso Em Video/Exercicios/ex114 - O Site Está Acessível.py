import urllib.request # Importando o módulo request da biblioteca urllib.

print('===== EXERCÍCIO #114 =====')
print()

try:
    site = urllib.request.urlopen('http://www.google.com') # Tentando abrir o site através da função urlopen().
except urllib.error.URLError: # Verificando se ocorreu algum erro.
    print('O site não está acessível no momento.')
else:
    print('O site está acessível.\n')
    print(site.read()) # Exibe todo o conteúdo do site (HTML).
