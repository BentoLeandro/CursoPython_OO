class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando o meroto nome property...")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando o metodo com setter...")
        self.__nome = nome   


cli1 = Cliente("bento")

print(cli1.nome)
cli1.nome = "teste"
print(cli1.nome)

