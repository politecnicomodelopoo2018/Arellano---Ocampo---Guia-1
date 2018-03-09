class alumno (object):
    nombre = None
    apellido = None
    fecha_de_nac = None
    lista_de_notas = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getapellido(self):
        return self.apellido

    def setFecha_de_nac(self, fechaNac):
        self.fecha_de_nac = fechaNac

    def getfechaNac(self):
        return self.fecha_de_nac



