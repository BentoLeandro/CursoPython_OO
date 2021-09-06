class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelum...')

    def buscar_cursos_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}'if mes else 'Mostrando cursos desse mês...')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alura...')

    def buscar_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum...')

class Hipster:
    def __str__(self):
        return f'Hipster {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

print('Funcionario Pleno----Jose----')
jose = Junior('Jose')
jose.buscar_perguntas_sem_resposta()
jose.mostrar_tarefas()

print('Funcionario Pleno----Luan----')
luan = Pleno('Luan')
luan.buscar_perguntas_sem_resposta()
luan.buscar_cursos_mes()
luan.mostrar_tarefas()

print('Funcionario Senior------Maria-----')
maria = Senior('Maria')
print(maria)

#MRO
#pleno > Alura > Funcionario > Caelum > Funcionario
