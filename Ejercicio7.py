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

def CrearProfesor (Sis):
    P = Profesor
    print("Ingrese el nombre:")
    P.setNombre(input())
    print("Ingrese el apellido:")
    P.setApellido(input())
    print("Ingrese el descuento")
    P.setDescuento(input())
    Sis.listaPersonas.append(P)

def CrearPlato (Sis):
    print("Ingrese fechaCreacion")




    self.fechaCreacion = fechaCreacion
    self.plato = plato
    self.persona = persona
    self.horaDeEntrega = horaDeEntrega
    self.entregado = False

def ModificarPersona (sis, nombre):
    A = 0
    for item in sis.listaPersonas:
        if item.nombre == nombre:
            while type(item) is Alumno and A != "4":
                print("1- Modificar Nombre")
                print("2- Modificar Apellido")
                print("3- Modificar Division")
                print("4- Volver")
                A = input()
                if A == "1":
                    print("Nombre nuevo")
                    B = input()
                    item.nombre.setNombre(B)
                if A == "2":
                    print("Apellido nuevo")
                    B = input()
                    item.nombre.setApellido(B)
                if A == "3":
                    print("Division nuva")
                    B = input()
                    item.nombre.setDivision(B)

            while item is Profesor and A != "4":
                print("1-Modificar Nombre")
                print("2-Modificar Apellido")
                print("3-Modificar Descuento")
                print("4-Salir")
                A = input()
                if A == "1":
                    print("Nombre nuevo")
                    B = input()
                    item.setNombre(B)
                if A == "2":
                    print("Apellido nuevo")
                    B = input()
                    item.setApellido(B)
                if A == "3":
                    print("Descuento nuevo")
                    B = input()
                    item.setDescuento(B)

def ModificarPlato (sis, nombre):
    for item in sis.bufet.listaPlatos:
        if item.nombre == nombre:
            while A != "3":
                print("1-Modificar nombre")
                print("2-Modificar precio")
                print("3-Salir")
                A = input()
                if A == "1":
                    print("Nombre nuevo")
                    B = input()
                    item.setNombre(B)
                if A == "2":
                    print("Precio nuevo")
                    B = input()
                    item.setPrecio(B)

def ModificarPedido (sis, persona):
    for item in sis.bufet.listaPedidos:
        if item.persona == persona:
            while A != "6":
                print("1-Modificar fechaCreacion")
                print("2-Modificar plato")
                print("3-Modificar persona")
                print("4-Modificar horaEntrega")
                print("5-Modificar entregado")
                print("6-Salir")
                A = input()
                if A == "1":
                    print("FechaCreacion nueva")
                    B = input()
                    item.setFechaCreacion(B)
                if A == "2":
                    print("Plato nuevo")
                    B = input()
                    item.setPlato(B)
                if A == "3":
                    print("Persona nueva")
                    B = input()
                    for met in sis.listaPersonas:
                        if met == B:
                            item.setPersona = met
                if A == "4":
                    print("Hora nueva")
                    B = input()
                    item.setHoraEntrega(B)
                if A == "5":
                    print("1-Entregado")
                    print("2-No entregado")
                    B = input()
                    if B == "1":
                        item.setEntregado(True)
                    if B == "2":
                        item.setEntregado(False)

def EliminarDeListaPersona (Sis):
    print("Ingrese la persona a borrar")
    temp = input()
    for item in Sis.listaPersonas:
        if item.nombre == temp:
            Sis.listaPersonas.remove(item)



