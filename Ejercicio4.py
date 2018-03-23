from calendar import monthrange
import datetime

class Empleado(object):

    nombre = None
    apellido = None
    telefono = None
    fechaNac = None

    def __init__(self):
        self.listaHorario = []
        self.listaAsistencia = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setFechaNac(self, fechaNac):
        self.fechaNac = fechaNac

    def setListaHorario(self, horario):
        self.listaHorario = (horario)

    def setListaAsistencia(self, listaAsistencia):
        self.listaAsistencia = listaAsistencia

    def getPorcentajeAsistenciaMensual(self, año, mes):
        a = 0
        b = 0
        for fecha in self.listaAsistencia:
            if fecha.year == año and fecha.month == mes:
                if self.listaHorario[fecha.weekday()]:
                    a = a + 1
        for d in range(1, monthrange(año, mes)[1] + 1):
            f = datetime.date(año, mes, d).weekday()
            if self.listaHorario[f]:
                b = b + 1
        a = a / b
        return a

class Empresa(object):

    def __init__(self):
       self.listaEmpleados = []

    def AgregarEmpleado(self, empleado):
        self.listaEmpleados.append(empleado)


    def asistenciaMensual(self, año, mes, nombre):
        for item in self.listaEmpleados:
            if item.nombre == nombre:
                a = item.getPorcentajeAsistenciaMensual(año,mes)
                return a
