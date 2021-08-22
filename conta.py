#from teste import deposita


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"construindo o objeto...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #self.__codigo_banco = "001"

    def extrato(self):
        return print(f"Saldo.: {self.__saldo} do titular.: {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_sacar <= valor_disponivel

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor 
        else:
            print(f"O valor {valor} passou do Limite!")    

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

    @staticmethod
    def codigo_banco():
        return "001" #self.__codigo_banco   

    @staticmethod
    def codigos_bancos():
        return {'BB':'001','Caixa':104,'Bradesco':'237'}          


from conta import Conta

Conta.codigo_banco()
Conta.codigos_bancos()

#conta1 = Conta(123, "Bento", 23.34, 2000.00)
#conta2 = Conta(222, "Maria", 100.00, 3000.00)


"""
print("*"*30)
print(conta1.saldo)
print(conta1.titular)
print(conta1.limite)

#conta1.limite = 6000.00

print(conta1.limite)
print("*"*30)

conta1.sacar(4000.00)
print(conta1.saldo)

conta2.transferir(30, conta1)

#print(conta)
#print(conta.depositar(100))
print(conta1.extrato())
#print(conta.sacar(50))
#print(conta.extrato())
print(conta2.extrato())
"""
