class Persona (object):
    nombre = None
    apellido = None

    def setNombre (self, nombre):
        self.nombre = nombre

    def setApellido (self, apellido):
        self.apellido = apellido


class Alumno (Persona):
    division = None

    def setDivision (self, division):
        self.division = division


class Profesor (Persona):
    descuento = None

    def setDescuento (self, descuento):
        self.descuento = descuento