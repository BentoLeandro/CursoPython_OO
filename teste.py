def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é.: {}".format(conta["saldo"]))    

conta = cria_conta(123, "Bento", 123.9, 2000.00)

deposita(conta, 500.00)
extrato(conta)

sacar(conta, 100)
extrato(conta)





