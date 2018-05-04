class Pedido (object):
    fechaCreacion = None
    plato = None
    persona = None
    horaDeEntrega = None
    entregado = False

    def setFechaCreacion (self, fecha):
        self.fechaCreacion = fecha

    def setPlato (self, plato):
        self.plato = plato

    def setPersona (self, persona):
        self.persona = persona

    def setHoraEntrega (self, hora):
        self.horaDeEntrega = hora

    def setEntregado (self, entregado):
        self.engregado = entregado