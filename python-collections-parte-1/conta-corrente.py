from functools import total_ordering

@total_ordering
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self.codigo, self.saldo)

    def __eq__(self, other):
        return self.saldo == other.saldo and self.codigo == other.codigo

    def __lt__(self, other):
        if self.saldo != other.saldo:
            return self.saldo < other.saldo
        return self.codigo < other.codigo

conta_do_gui = ContaCorrente(12)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(95)
conta_da_dani.deposita(1000)

conta_do_paulo = ContaCorrente(64)
conta_do_paulo.deposita(450)

contas = [conta_do_gui, conta_da_dani]

print("Mostrando contas")
for conta in contas:
    print(conta)

print()
print ("verificando validações")
print(conta_do_gui > conta_do_paulo)