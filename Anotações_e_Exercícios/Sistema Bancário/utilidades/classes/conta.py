from abc import ABC, abstractmethod


class Conta(ABC):
    """
    Esta é uma classe abstrata que representa uma conta bancária.
    """
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property  # Decorator para indicar que o método é um atributo (criando um getter).
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):  # Verificando se a instância do valor é um inteiro ou float.
            raise ValueError('O valor a ser depositado deve ser um número.')  # Lançando uma excessão caso o valor seja inválido.
        self._saldo += valor

    @abstractmethod  # Decorator para indicar que o método é um método abstrato.
    def sacar(self, valor):
        pass
