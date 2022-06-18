"""
Singleton: Este padrão de design consiste em criar uma classe que contenha uma única instancia para multiplos objetos.
Normalmente utilizado em classes de banco de dados, no intuito de manter os recursos sempre sincronizados.
- Funcionamento:
    - O objeto é criado quando a classe é instanciada pela primeira vez.
    - O objeto é mantido em memória até o programa terminar.
    - Caso outro objeto tente instanciar a mesma class, a instância do objeto já existente é retornada.
- Detalhes:
    - O método __new__ é o responsável por criar a class. quando a class é criada, o método __init__ é chamado.
        - O método __new__ pode ser modificado, mas ele cria a class, então precisa funcionar corretamente. 
            - Tudo que estiver dentro do __new__ será criado dentro da class.
            - Uma forma de modificar o __new__ e ainda funcionar corretamente, é chamando o __new__ da class padrão do python (object).
    - No padrão Singleton, o método __new__ cria uma instância na primeira vez que é chamado. e nas próximas vezes, ele verifica se já existe e retorna a instância existente.
"""

class Singleton:
    def __new__(cls, *args, **kwargs):
 
        if not hasattr(cls, '_jaexiste'):  # Verificando se o atributo de class "_jaexiste" não existe.
            cls._jaexiste = object.__new__(cls)  # Criando o atributo de class e atribuindo uma nova instância.
     
        return cls._jaexiste  # retornando a instância da class
 
 
item1 = Singleton()
item2 = Singleton()

print('\nOs objetos são iguais? ', item1 == item2)  # Saída: Os objetos são iguais?  True
print("\nOs ID's são iguais? ", id(item1) == id(item2))  # Saída: Os ID's são iguais?  True

print(f'\nIDs: item1 - {id(item1)} | Item2 - {id(item2)}')  # Saída: IDs: Item1 - ID | Item2 - ID
print(f'\nObjetos: item1 - {item1} | item2 - {item2}\n')  # Saída: Objetos: item1 - <Obj_Mem> | item2 - <Obj_Mem>
