class Alumno (object):
    nombre = None
    apellido = None
    fecha_de_nac = None

    def __init__(self):
        self.lista_de_notas = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFecha_de_nac(self, fecha):
        self.fecha_de_nac = fecha

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

    def promedioNotas(self):
        if len(self.lista_de_notas) == 0:
            return False
        return sum(self.lista_de_notas) / len(self.lista_de_notas)




    def getNombre(self):
        return self.nombre

    def getapellido(self):
        return self.apellido