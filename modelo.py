from abc import ABCMeta, abstractmethod
#abs = Abstract Base Classes

class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome        

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1    

    #metodo especial para representar de forma textual o objeto
    @abstractmethod
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} likes'    

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes'    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) #executa o inicializador da classe Pai
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes'        

class Playlist:
    def __init__(self, nome, programas):                
        self.nome = nome        
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item] 
    
    def __len__(self):
        return len(self._programas)    


vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
todo_m_panico = Filme('Todo Mundo em Panico', 2000, 120)
sobre_natural = Serie('Sobre Natural', 2002, 18)


vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

todo_m_panico.dar_like()
todo_m_panico.dar_like()
todo_m_panico.dar_like()

sobre_natural.dar_like()
sobre_natural.dar_like()

filmes_series = [vingadores, atlanta, todo_m_panico, sobre_natural]

favoritos = Playlist('Favoritos top 4', filmes_series)

print(f'Tamanho.: {len(favoritos)}')
for programa in favoritos:    
    print(programa)

print(f'Vingadores está na lista ?.: {vingadores in favoritos}')    
