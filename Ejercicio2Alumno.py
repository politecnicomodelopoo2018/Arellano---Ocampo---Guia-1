from Ejercicio2Materia import Materia

class Alumno (object):
    nombre = None
    apellido = None
    fecha_de_nac = None

    def __init__(self):
        self.lista_de_materias = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFecha_de_nac(self, fecha):
        self.fecha_de_nac = fecha

    def agregarMateria(self, nombremateria):
        unaM = Materia(nombremateria)
        self.lista_de_materias.append(unaM)

    def agregarNota(self, nota, nombremateria):
        for n in self.lista_de_materias:
            if nombremateria != self.lista_de_materias[n].nombre:
                return False
            self.lista_de_materias[n].agregarNota(nota)

    def promedioNotasMateria(self, nombremateria):
        for n in self.lista_de_materias:
            if self.lista_de_materias[n].nombre == nombremateria:
                if len(self.lista_de_materias) == 0:
                    return False
                return sum(self.lista_de_materias[n].lista_de_notas) / len(self.lista_de_materias[n].lista_de_notas)











    def agregarNota(self, nota):
        if nota > 10 or nota < 1:
            return False
        self.lista_de_notas.append(nota)

    def mayorNota(self):
        if len(self.lista_de_notas) == 0:
            return False
        return max(self.lista_de_notas)

    def menorNota(self):
        if len(self.lista_de_notas) == 0:
            return False
        return min(self.lista_de_notas)

