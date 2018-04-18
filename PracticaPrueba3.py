class Empleado(object):

    def __init__(self, nombre, apellido, DNI, pais, numTel):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.pais = pais
        self.numTel = numTel

class Empresa(object):

    def __init__(self):
        self.empleados = []
        self.listaLlamadas = []

    def setEmpleados(self, empleados):
        self.empleados = empleados

    def addEmpleado(self, empleado):
        self.empleados.append(empleado)

    def setListaLlamadas(self, listaLlamadas):
        self.listaLlamadas = listaLlamadas

    def llamar(self, numOrig, numDest):
        llamada = Llamada()
        for item in self.empleados:
            if item.numTel == numDest:
                llamada.emplD = item
            if item.numTel == numOrig:
                llamada.emplO = item
        llamada.fecha = Now()
        return llamada

    def colgar(self, llamada):
        llamada.duracion = now() - llamada.fecha
        self.listaLlamadas.append(llamada)


    def llamadas_empleados(self, empleado):
        lista = []
        for item in self.listaLlamadas:
            if item.emplO == empleado:
                lista.append(item)
        return lista

    def tiempoExt(self, empleado):
        valor = 0
        for item in self.llamadas_empleados(empleado):
            if item.emplO.pais != item.emplD.pais:
                valor += item.duracion


class Llamada(object):

    def __init__(self, emplO, emplD, fecha, duracion):
        self.emplO = emplO
        self.emplD = emplD
        self.fecha = fecha
        self.duracion = duracion
