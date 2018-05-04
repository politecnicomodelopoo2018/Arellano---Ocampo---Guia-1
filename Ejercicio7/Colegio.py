class Colegio (object):

    def __init__(self, bufet):
        self.listaPersonas = []
        self.bufet = bufet

    def addPersona (self, persona):
        self.listaPersonas.append(persona)

    def setBufet (self, bufet):
        self.bufet = bufet