from utilidades.classes.conta import Conta


class ContaCorrente(Conta):
    """
    Esta classe representa uma conta corrente que herda da classe abstrata Conta.
    - Esta classe recebe:
        - O construtor da classe Conta.
        - O método depositar da classe Conta.
        - O método abstrato sacar da classe Conta.
    - Esta classe sobrescreve:
        - O construtor da classe Conta.
            - Adicionando um parâmetro limite.
        - O método sacar da classe Conta.
            - Adicionando a verificação do saldo com o limite.
    """
    def __init__(self, agencia, conta, saldo, limite=100):  # Sobrescrevendo o método __init__ da classe Conta.
        super().__init__(agencia, conta, saldo)  # Passando os parâmetros para o método __init__ da classe Conta através do super().
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self._saldo + self._limite) < valor:
            raise ValueError('Saldo insuficiente.')
        
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor a ser sacado deve ser um número.')

        self._saldo -= valor
