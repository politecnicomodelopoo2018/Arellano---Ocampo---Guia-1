class Persona (object):
    nombre = None
    apellido = None

    def setNombre (self, nombre):
        self.nombre = nombre

    def setApellido (self, apellido):
        self.apellido = apellido

    def getDescuento(self):
        return 0

    def pasarGuardar(self):
        return(self.__class__.__name__+"|"+self.nombre + "|" + self.apellido + "|" + "\n")

    def loadFromString(self, datos):
        self.setNombre(datos[1])
        self.setApellido(datos[2])


class Alumno (Persona):
    division = None

    def setDivision (self, division):
        self.division = division

    def pasarGuardar(self):
        return(self.__class__.__name__+"|" + self.nombre + "|" + self.apellido + "|" + self.division + "\n")

    def loadFromString(self, datos):
        Persona.loadFromString(self,datos)
        self.setDivision(datos[3])

class Profesor (Persona):
    descuento = None

    def setDescuento (self, descuento):
        self.descuento = descuento

    def getDescuento(self):
        return self.descuento

    def pasarGuardar(self):
        return(self.__class__.__name__+"|" + self.nombre + "|" + self.apellido + "|" + self.descuento + "\n")

    def loadFromString(self, datos):
        Persona.loadFromString(self, datos)
        self.setDescuento(datos[3])

