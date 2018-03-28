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

    def __init__(self):
        self.turno = []

    def setTurno(self, turno):
        self.turno = turno

class Partido(object):
    equipo1 = None
    equipo2 = None
    Dia = None

    def setEquipoA(self, equipo):
        self.equipoA = equipo

    def setEquipoB(self, equipo):
        self.equipoB = equipo

    def setDia(self, dia):
        self.Dia = dia

class Torneo(object):

    def __init__(self):
        self.listaEquipos = []
        self.listaPartidos = []

    def setListaEquipos(self, listaequipos):
        self.listaEquipos = listaequipos

    def añadirAListaPartidos(self, partido):
        self.listaPartidos.append(partido)

    def buscarIgual(self, equipoA, equipoB):
        for partido in self.listaPartidos:
            if (equipoA == partido.equipo1 and equipoB == partido.equipo2) or (equipoA == partido.equipo2 and equipoB == partido.equipo1):
                return False
            return True

    def fixture(self):
        partido = Partido()
        for equipo in self.listaEquipos:
            for equipo2 in self.listaEquipos:
                if (equipo2 == equipo) or (self.buscarIgual(equipo, equipo2) == False):
                    continue
                for dia in range(6):
                    for turno in range(3):
                        if equipo2.listaHorarios[dia][turno] and equipo.listaHorarios[dia][turno]:
                            partido.equipoA = equipo
                            partido.equipoB = equipo2
                            partido.Dia = equipo.listaHorarios[dia]
                            self.añadirAListaPartidos(partido)







