from abc import ABCMeta, abstractmethod

#quando a classe for abstrata ela nunca vai ser instanciada diretamente com o objeto
class Pessoa(metaclass = ABCMeta):
    def __init__(self, nome, fone, situacao):
        self._nome = nome
        self._fone = fone
        self._situacao = situacao

    #duck typing
    @abstractmethod
    def __str__(self):
        return f"Pessoa.: {self._nome} Fone.: {self._fone} Situação.: {self._situacao}"

    #metodo estatico.. o metodo é da classe e nao do objeto.
    @staticmethod
    def tipos_pessoas():
        return f"J-Juridica e F - Fisica"    

    @property
    def nome(self):
        return self._nome  

    @nome.setter
    def nome(self, valor):
        self._nome = valor          


class PessoaFisica(Pessoa):
    def __init__(self, nome, fone, situacao, cpf, rg, data_nascimento):
        super().__init__(nome, fone, situacao)
        self._cpf = cpf
        self._rg = rg
        self._data_nascimento = data_nascimento

    #polimorfismo
    def __str__(self):
        return f"Nome.: {self._nome} Fone.: {self._fone} Sit.: {self._situacao} CPF.: {self._cpf}"

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        self._cpf = valor

    @property
    def rg(self):
        return self._rg

    @rg.setter
    def rg(self, valor):
        self._rg = valor    

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor):
        self._data_nascimento = valor    

class PessoaJuridica(Pessoa):
    def __init__(self, nome, fone, situacao, cnpj, insc_estadual):
        super().__init__(nome, fone, situacao)
        self._cnpj = cnpj
        self._insc_estadual = insc_estadual

    def __str__(self):
        return f"Nome.: {self._nome} Fone.: {self._fone} Pessoa Juridica"    

    @property
    def cnpj(self):
        return self._cnpj    

    @cnpj.setter
    def cnpj(self, valor):
        self._cnpj = valor

    @property
    def insc_estadual(self):
        return self._insc_estadual    

    @insc_estadual.setter
    def insc_estadual(self, valor):
        self._insc_estadual = valor     

#pessoa1 = Pessoa("leandro", "99986-1299", "A")

#print(pessoa1)
#print(pessoa1.nome)
#pessoa1.nome = "Leandro Reis Bento"
#print(pessoa1)

fisica1 = PessoaFisica("Bento", "9988-7766", "A", "089.890.098-09", "9887878", "20/02/1990")
print(fisica1)
print(fisica1.tipos_pessoas())

juridica1 = PessoaJuridica("teste", "teste", "A", "989898998", "98989898")
print(juridica1)