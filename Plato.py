class Plato (object):
    nombre = None
    precio = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrecio(self, precio):
        self.precio = precio

    def pasarGuardar(self):
        return(self.nombre + "|" + self.precio + "\n")