from utilidades.classes.conta import Conta


class ContaCorrente(Conta):
    """
    Classe Conta Corrente que herda de Conta

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
    
    Atributos
    ---------
    agencia : str
        chave da agência
    conta : str
        chave da conta
    saldo : float
        saldo da conta
    limite : int
        limite da conta (padrão 100)

    Métodos
    -------
    limite(getter)
        Coleta a chave da agência
    sacar(valor)
        Subtrai valores do saldo da conta.
    """
    def __init__(self, agencia: str, conta: str, saldo: float, limite: int=100):  # Sobrescrevendo o método __init__ da classe Conta.
        """
        Sobrescreve o inicializador da Conta

        Este inicializador sobrescreve o inicializador da Abstract Class Conta e insere o atributo limite
        """
        super().__init__(agencia, conta, saldo)  # Passando os parâmetros para o método __init__ da classe Conta através do super().
        self._limite = limite

    @property
    def limite(self) -> int:
        return self._limite

    def sacar(self, valor: float) -> None:
        """
        Este método sobrescreve o método abstrato da class Conta.

        Parametros
        ----------
            valor : float
                Valor a subtrair
        
        Retorno
        -------
            None
        """
        if (self._saldo + self._limite) < valor:
            raise ValueError('Saldo insuficiente.')
        
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor a ser sacado deve ser um número.')

        self._saldo -= valor
