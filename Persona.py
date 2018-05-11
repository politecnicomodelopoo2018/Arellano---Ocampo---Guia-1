class Persona(object):
    dni = None
    nombre = None
    apellido = None
    fechaIngreso = None

    def setDni(self,dni):
        self.dni = dni

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellido(self,apellido):
        self.apellido = apellido

    def setFechaIngreso(self,fechaIngreso):
        self.fechaIngreso = fechaIngreso

class Conductor(Persona):
    pass

class Musicalizador(Persona):
    pass

class OpTecnico(Persona):
    pass