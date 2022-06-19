"""
Este módulo contém a classe abstrata Conta

A classe Conta está herdando da classe abstrata ABC do módulo abc e contém um método decorado como @abstractmethod para fazer com que ela não seja instanciável e também para fazer as classes filhas dela sobrescrevam o método decorado.
"""
from abc import ABC, abstractmethod


class Conta(ABC):
    """
    Esta é uma classe abstrata que representa uma conta bancária.

    Atributos
    ---------
    agencia : str
        chave da agência
    conta : str
        chave da conta
    saldo : float
        saldo da conta

    Métodos
    -------
    agencia(getter)
        Coleta a chave da agência
    conta(getter)
        Coleta a chave da conta.
    saldo(getter)
        Coleta o saldo da conta
    depositar(valor)
        Adiciona valores ao saldo da conta.
    sacar(valor)
        Subtrai valores do saldo da conta.
    """
    def __init__(self, agencia: str, conta: str, saldo: float):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property  # Decorator para indicar que o método é um atributo (criando um getter).
    def agencia(self) -> str:
        return self._agencia

    @property
    def conta(self) -> str:
        return self._conta

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> None:
        """
        Este método adiciona valores a conta.

        Parametros
        ----------
            valor : float
                Valor do depósito.
        
        Retorno
        -------
            None
        """
        if not isinstance(valor, (int, float)):  # Verificando se a instância do valor é um inteiro ou float.
            raise ValueError('O valor a ser depositado deve ser um número.')  # Lançando uma excessão caso o valor seja inválido.
        self._saldo += valor

    @abstractmethod  # Decorator para indicar que o método é um método abstrato.
    def sacar(self, valor: float) -> None:
        """
        Este método abstrato subtrai valores da conta.

        Parametros
        ----------
            valor : float
                Valor a subtrair
        
        Retorno
        -------
            None
        """
        pass
