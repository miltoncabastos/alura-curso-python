class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("contruindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001 - Banco do Brasil"

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if(self.__validarSaque(valor)):
            self.__saldo -= valor
        else:
            print("Saldo insuficiênte para saque")

    def __validarSaque(self, valor):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor <= valor_disponivel_para_saque

    def receber_transferencia(self, valor, origem):
        origem.sacar(valor)
        self.depositar(valor)

    @property
    def titular(self):
        return self.__titular.title()

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

contaMilton = Conta(956, "milton bastos", 600.0, 1000.0)
contaJoao = Conta(136, "joão celestino", 500.0, 1000.0)

print(contaMilton.extrato())
print(contaJoao.extrato())
contaMilton.receber_transferencia(50, contaJoao)
contaMilton.titular = "MiltãoFC"
print(contaMilton.extrato())
print(contaJoao.extrato())
print(Conta.codigo_banco())