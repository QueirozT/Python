from ex112.utilidades import moedas # Importando da pasta ex112 no pacote "utilidades" o módulo "moedas".
from ex112.utilidades import dados # importando o módulo "dados" do pacote "utilidades" para validar a entrada de dados.

print('===== EXERCÍCIO #110 =====')
print()

v = dados.leiaDinheiro('Digite o preço: R$')

moedas.resumo(v, 80, 35)
print()
