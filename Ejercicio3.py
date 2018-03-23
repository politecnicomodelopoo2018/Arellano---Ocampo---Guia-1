class Jugador(object):
    nombre = None
    fechaNac = None
    nCamiseta = None
    capitan = False

    def setNombre(self, nombre):
        self.nombre = nombre

    def setFechaNac(self, fecha):
        self.fechaNac = fecha

    def setNCamiseta(self, num):
        self.nCamiseta = num

    def setCapitanState(self, state):
        self.capitan = state

class Equipo(object):
    barrio = None
    nombre = None
    def __init__(self):
        self.listaJugadores = []
        self.listaHorarios = []

    def setBarrio(self, barrio):
        self.barrio = barrio

    def setNombre(self, nombre):
        self.nombre = nombre

    def setListaJugadores(self, listaJugadores):
        self.listaJugadores = listaJugadores

    def setListaHorarios(self, listaHorarios):
        self.listaHorarios = listaHorarios

    def agregarJugador(self, jugador):
        if len(self.listaJugadores) == 10:
            return False
        for item in self.listaJugadores:
            if jugador.capitan and item.capitan:
                return False
            if item.nCamiseta == jugador.nCamiseta:
                return False
        self.listaJugadores.append(jugador)
        return True

class Dia(object):
    mañana = None
    tarde = None
    noche = None

    def setManTarNoch(self, mañana, tarde, noche):
        self.mañana = mañana
        self.tarde = tarde
        self.noche = noche

class Torneo(object):

    def __init__(self):
        self.listaEquipos = []

