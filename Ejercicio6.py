class Empresa (object):
    def __init__(self):
        self.listaAutos = []
        self.listaCamionetas = []

class Vehiculo (object):
    def __init__(self, Patente, CantRuedas, AñoFabricacion):
        self.patente = Patente
        self.cantRuedas = CantRuedas
        self.añoFabricacion = AñoFabricacion

class Camioneta (Vehiculo):
    def __init__(self, Patente, CantRuedas, AñoFabricacion, CapacidadCargaKg):
        super().__init__(self, Patente, CantRuedas, AñoFabricacion)
        self.CapacidadCargaKg = CapacidadCargaKg

class Auto (Vehiculo):
    def __init__(self, Patente, CantRuedas, AñoFabricacion, Descapotable):
        super().__init__(self, Patente, CantRuedas, AñoFabricacion)
        self.descapotable = Descapotable
