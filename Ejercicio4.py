import datetime

class empleado(object):

    nombre = "Jorge"
    apellido = "Ocampo"
    telefono = 12344112
    fechaNac = "2001-05-13"

    def __init__(self):
        self.listaHorario = [True, True, True, True, True, False, False]
        self.listaAsistencia = [fecha fecha fecha]


class empresa(object):

    def __init__(self):

       self.listaEmpleados = []

    def fuecuandolecorrespondiaono(self, nombre, fecha):
        for item in self.listaEmpleados:
            if item.nombre == nombre:
                if(item.listaHorario[fecha.weekday()] == False):
                    return False
                return True

    def asistenciaMensual(self, año, mes, nombre):
        for item in self.listaEmpleados:
            if item.nombre == nombre:
                for fecha in item.listaAsistencia:
                    if (fecha)





