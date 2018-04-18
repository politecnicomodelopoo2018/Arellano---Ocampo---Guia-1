class Persona (object):

    def __init__(self, nombre, apellido, fechanac):
        self.nombre = nombre
        self.apellido = apellido
        self.fechanac = fechanac








class Artista (Persona):
    pass







class Autor (Persona):

    def __init__(self, nombre, apellido, fechanac, nacionalidad):
        Persona.__init__(self, nombre, apellido, fechanac)
        self.nacionalidad = nacionalidad






class Cancion (object):

    def __init__(self, titulo):
        self.titulo = titulo
        self.listaAr = []
        self.listaAu = []









class Album (object):

    def __init__(self, titulo):
        self.titulo = titulo
        self.listaCa = []

    def GetArtAll(self):

        listArt = []

        for i in self.listaCa:
            for i2 in i.listaAr:
                if i2 not in listArt:
                    self.listArt.append(i2)

        return listArt

    def GetArtInf (self, listaCa):

        listArt = []

        cont = 0

        for i in self.listaCa:
            for i2 in listArt:
                if i == i2:
                    cont += 1











class Sistema (object):
    def __init__(self):
        self.listAl = []

