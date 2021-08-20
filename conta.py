from teste import deposita


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"construindo o objeto...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        return print(f"Saldo.: {self.__saldo} do titular.: {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor 

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite 

    @limite.setter
    def limite(self, valor):
        self.__limite = valor           

conta1 = Conta(123, "Bento", 23.34, 2000.00)
conta2 = Conta(222, "Maria", 100.00, 3000.00)


print("*"*30)
print(conta1.saldo)
print(conta1.titular)
print(conta1.limite)

conta1.limite = 6000.00

print(conta1.limite)
print("*"*30)


conta2.transferir(30, conta1)

#print(conta)
#print(conta.depositar(100))
print(conta1.extrato())
#print(conta.sacar(50))
#print(conta.extrato())
print(conta2.extrato())

