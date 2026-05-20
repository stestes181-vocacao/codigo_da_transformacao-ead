class SaldoInsuficienteError(Exception):
    pass
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):

        if valor > self.saldo:
            raise SaldoInsuficienteError(
                "❌ Saldo insuficiente para realizar o saque."
            )

        self.saldo -= valor

        print("💸 Saque realizado com sucesso.")
        print(f"💰 Saldo atual: R${self.saldo}")

#sefira: codinome for stefani.
conta = ContaBancaria("Sefira", 1500)

try:
    conta.sacar(1700)

except SaldoInsuficienteError as erro:
    print(erro)