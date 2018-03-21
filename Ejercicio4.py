import datetime
from calendar import monthrange

class Empleado(object):

    nombre = "Jorge"
    apellido = "Ocampo"
    telefono = 12344112
    fechaNac = "2001-05-13"

    def __init__(self):
        self.listaHorario = [True, True, True, True, True, False, False]
        self.listaAsistencia = [datetime.date(2011,10,1), datetime.date(2011,10,2), datetime.date(2011,10,3), datetime.date(2011,10,4), datetime.date(2011,10,5), datetime.date(2012,10,1), datetime.date(2011,11,1)]


class Empresa(object):

    def __init__(self, empleado):

       self.listaEmpleados = [empleado]

    def fuecuandolecorrespondiaono(self, nombre, fecha):
        for item in self.listaEmpleados:
            if item.nombre == nombre:
                if item.listaHorario[fecha.weekday()] == False:
                    return False
                return True

    def asistenciaMensual(self, año, mes, nombre):
        a = 0
        b = 0
        for item in self.listaEmpleados:
            if item.nombre == nombre:
                for fecha in item.listaAsistencia:
                    if fecha.year == año and fecha.month == mes:
                        if item.listaHorario[fecha.weekday()]:
                            print("a ahora:", a)
                            a = a+1
                for d in range(1, monthrange(año, mes)[1]+1):
                    f = datetime.date(año, mes, d).weekday()
                    if item.listaHorario[f]:
                        b = b + 1
                        print("b", b)
                print("a:", a)
                print("b:", b)
                a = a / b
                return a
