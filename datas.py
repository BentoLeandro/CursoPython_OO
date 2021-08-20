class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__Python = 0

    def formatada(self):
        print(f"{self.__dia}/{self.__mes}/{self.__ano} {self.__Python} 0/")


class Retangulo:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__are = x * y

    def obter_area(self):
        return self.__are


r = Retangulo(7, 6)  
r.are = 7
print(r.obter_area()) 
print(r.are)



teste = Data(20, "02", 1990)

teste.formatada()
#print(teste.__mes)

