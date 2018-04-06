from datetime import date
class Humano(object):
    nombre = None
    apellido = None
    fechanac = None

    def __init__(self):
        self.pesaje = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFechanac(self, fechanac):
        self.fechanac = fechanac

    def setPesaje(self, pesaje):
        self.pesaje = pesaje

    def addPesaje(self, pesaje):
        self.pesaje.append(pesaje)

    def getStatFecha(self, fecha):
        for item in self.pesaje:
            if fecha == item.fechatest:
                return item

    def getPromedioAño(self, año):
        cant = 0
        sumalt = 0
        sumpes = 0
        devuelve = Stats(None, None, None)
        for item in self.pesaje:
            if año == item.fechatest.year:
                cant += 1
                sumalt += item.altura
                sumpes += item.peso
        devuelve.peso = sumpes/cant
        devuelve.altura = sumalt/cant
        return devuelve

    def getCrecimiento(self, añoA, añoB):
        return ((self.getPromedioAño(añoB).altura * 100) / self.getPromedioAño(añoA).altura) - 100


class Stats(object):

    def __init__(self, peso, altura, fechatest):
        self.altura = altura
        self.fechatest = fechatest
        self.peso = peso