class Programa(object):
    nombre = None
    opTec = None
    categoria = None

    def __init__(self):
        self.listaConductores = []
        self.listaHorarios = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setOpTec(self,opTec):
        self.opTec = opTec

    def setCategoria(self,categoria):
        self.categoria = categoria

    def addConductor(self, conductorDni, radio):
        for item in radio.listaGente:
            if item.dni == conductorDni:
                self.listaConductores.append(item)

    def addHorario(self, horario):
        self.listaHorarios.append(horario)

class ProgramaMusica(Programa):
    musicalizador = None

    def __init__(self):
        super().__init__(self)
        self.listaEstilos = []

    def setMusicalizador(self, musicalizadorDni, radio):
        for item in radio.listaGente:
            if item.dni == musicalizadorDni:
                self.musicalizador = item

    def addEstilo(self, estilo):
        self.listaEstilos.append(estilo)


        




