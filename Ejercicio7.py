class Persona (object):
    nombre = None
    apellido = None

    def setNombre (self, nombre):
        self.nombre = nombre

    def setApellido (self, apellido):
        self.apellido = apellido

class Alumno (Persona):
    division = None

    def setDivision (self, division):
        self.division = division

class Profesor (Persona):
    descuento = None

    def setDescuento (self, descuento):
        self.descuento = descuento

class Plato (object):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido (object):

    def __init__(self, fechaCreacion, plato, persona, horaDeEntrega):
        self.fechaCreacion = fechaCreacion
        self.plato = plato
        self.persona = persona
        self.horaDeEntrega = horaDeEntrega
        self.entregado = False

    def entregado (self):
        self.engregado = True

class Bufet (object):

    def __init__(self):
        self.listaPlatos = []
        self.listaPedidos = []

    def addPlato (self, plato):
        self.listaPlatos.append(plato)

    def addPedido (self, pedido):
        self.listaPedidos.append(pedido)

class Colegio (object):

    def __init__(self, bufet):
        self.listaPersonas = []
        self.bufet = bufet

    def addPersona (self, persona):
        self.listaPersonas.append(persona)

    def setBufet (self, bufet):
        self.bufet = bufet


def CrearAlumno (Sis):
    A = Alumno()
    print("Ingrese el nombre:")
    A.setNombre(input())
    print("Ingrese el apellido:")
    A.setApellido(input())
    print("Ingrese la division")
    A.setDivision(input())
    Sis.listaPersonas.append(A)

def ModificarAlumno (Sis, nombre):
    for item in Sis:
        if item.nombre == nombre:



