class Bufet (object):

    def __init__(self):
        self.listaPlatos = []
        self.listaPedidos = []

    def addPlato (self, plato):
        self.listaPlatos.append(plato)

    def addPedido (self, pedido):
        self.listaPedidos.append(pedido)