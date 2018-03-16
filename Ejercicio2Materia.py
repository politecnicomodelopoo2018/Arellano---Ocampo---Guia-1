class Materia (object):

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_de_notas = []

    def agregarNota(self, nota):
        if nota > 10 or nota < 1:
            return False
        self.lista_de_notas.append(nota)

    def menorNota(self):
        if len(self.lista_de_notas ) == 0:
            return False
        return min(self.lista_de_notas)

    def promedioMateria(self):
        if len(self.lista_de_notas ) == 0:
            return False
        return sum(self.lista_de_notas)/len(self.lista_de_notas)