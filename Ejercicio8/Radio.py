class Radio(object):
    def __init__(self):
        self.listaProgramas = []
        self.listaGente = []

    def addToListaProgramas(self, programa):
        self.listaProgramas.append(programa)

    def addToListaGente(self,gente):
        self.listaGente.append(gente)

    def compararHorarios(self, programaA, programaB):
        for horaA in programaA.listaHorarios:
            for horaB in programaB.listaHorarios:
                if horaA == horaB:
                    return False
        return True



