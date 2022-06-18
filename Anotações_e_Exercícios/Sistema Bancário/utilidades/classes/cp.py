from utilidades.classes.conta import Conta  # A importação usa a perspectiva do programa principal.


class ContaPoupanca(Conta):
    """
    Esta classe representa uma conta poupança que herda da classe abstrata Conta.
    - Esta classe recebe:
        - O construtor da classe Conta.
        - O método depositar da classe Conta.
        - O método abstrato sacar da classe Conta.
    - Esta classe sobrescreve:
        - O método abstrato sacar da classe Conta.
    """
    def sacar(self, valor):  # Sobrescrevendo o método abstrato sacar da classe Conta.
        if self._saldo < valor: 
            raise ValueError('Saldo insuficiente.')  # Lançando uma excessão caso o saldo seja insuficiente.
        
        if not isinstance(valor, (int, float)):  # Verificando se a instância do valor é um inteiro ou float.
            raise ValueError('O valor a ser sacado deve ser um número.')  # Lançando uma excessão caso o valor seja inválido.
        
        self._saldo -= valor
