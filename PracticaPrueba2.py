class Plato(object):
    nombre = None
    cantCal = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCantCal(self, cantCal):
        self.cantCal = cantCal

class Persona(object):
    nombre = None
    fechaNac = None

    def __init__(self):
        self.listaPlatos = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setFechaNac(self, fechaNac):
        self.fechaNac =fechaNac

    def setListaPlatos(self, lista):
        self.listaPlatos = lista

    def addPlato(self, plato):
        self.listaPlatos.append(plato)

    def calConsumidas(self):
        calorias = 0
        for item in self.listaPlatos:
            calorias += item.cantCal
        return calorias

class Familia(object):

    def __init__(self):
        self.integrantes = []

    def addIntegrante(self, integrante):
        self.integrantes.append(integrante)

    def getPromCal(self):
        calorias = 0
        for item in self.integrantes:
            calorias += item.calConsumidas()
        return calorias/len(self.integrantes)

    def getPersonaMax(self):
        primer = self.integrantes[0]
        for item in self.integrantes:
            if primer.calConsumidas() < item.calConsumidas():
                primer = item
        return primer

    def getPersonaMin(self):
        primer = self.integrantes[0]
        for item in self.integrantes:
            if primer.calConsumidas() > item.calConsumidas():
                primer = item
        return primer