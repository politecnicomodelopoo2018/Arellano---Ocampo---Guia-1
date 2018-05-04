from Ejercicio2.Ejercicio2Materia import Materia


class Alumno(object):
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
        for item in self.lista_de_materias:
            if item.nombre == nombremateria:
                item.agregarNota(nota)
                return True
        return False

    def promedioNotasMateria(self, nombremateria):
        for item in self.lista_de_materias:
            if item.nombre == nombremateria:
                if len(self.lista_de_materias) == 0:
                    return False
                return sum(item.lista_de_notas) / len(item.lista_de_notas)

    def menorNota(self):
        if len(self.lista_de_materias) == 0:
            return False
        m = self.lista_de_materias[0].menorNota()
        for item in self.lista_de_materias:
            if m > item.menorNota():
                m = item.menorNota()
        return m

    def promedio(self):
        if len(self.lista_de_materias) == 0:
            return False
        m = 0
        for item in self.lista_de_materias:
            m += item.promedioMateria()
        return m / len(self.lista_de_materias)

    def menorPromedio(self):
        if len(self.lista_de_materias) == 0:
            return False
        m = self.lista_de_materias[0].promedioMateria()
        for item in self.lista_de_materias:
            if m > item.promedioMateria():
                m = item.promedioMateria()
        return m

    def mayorPromedio(self):
        if len(self.lista_de_materias) == 0:
            return False
        m = self.lista_de_materias[0].promedioMateria()
        for item in self.lista_de_materias:
            if m < item.promedioMateria():
                m = item.promedioMateria()
        return m

