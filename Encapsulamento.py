class Conta:
    def __init__(self, nro_agencia, saldo=0) -> None:
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depesitar(self, valor):
        # ...
        self._saldo += valor

    def secar(self, valor):
        # ...
        self._saldo -= valor

    def mostra_saldo(self):
        # ...
        return self._saldo


conta = Conta('0001', 100)
conta.depesitar(100)
print(conta.nro_agencia)
print(conta.mostra_saldo())
