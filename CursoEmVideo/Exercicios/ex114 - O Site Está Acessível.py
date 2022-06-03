import urllib.request

print('===== EXERCÍCIO #114 =====')
print()

try:
    acesso = urllib.request.urlopen('http://www.google.com')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('O site está acessível.')
print()
