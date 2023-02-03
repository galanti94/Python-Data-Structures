# Usams _ para definir o que é privado; é uma convenção.
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        print(self._saldo)
    
    def sacar(self, valor):
        self._saldo -= valor
        print(self._saldo)


conta = Conta(1000)
conta.sacar(10)
conta.depositar(50)
