class Materia (object):

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_de_notas = []

    def agregarNota(self, nota):
        if nota > 10 or nota < 1:
            return False
        self.lista_de_notas.append(nota)