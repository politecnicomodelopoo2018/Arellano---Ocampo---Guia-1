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
        return(self.nombre + "|" + self.apellido + "|")


class Alumno (Persona):
    division = None

    def setDivision (self, division):
        self.division = division

    def pasarGuardar(self):
        return("a|" + self.nombre + "|" + self.apellido + "|" + self.division)


class Profesor (Persona):
    descuento = None

    def setDescuento (self, descuento):
        self.descuento = descuento

    def getDescuento(self):
        return self.descuento

    def pasarGuardar(self):
        return("p|" + self.nombre + "|" + self.apellido + "|" + self.descuento)