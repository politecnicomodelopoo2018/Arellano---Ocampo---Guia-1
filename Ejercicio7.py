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
    nombre = None
    precio = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrecio(self, precio):
        self.precio = precio

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
    A.setNombre(input("Ingrese el nombre:"))
    A.setApellido(input("Ingrese el apellido:"))
    A.setDivision(input("Ingrese la division"))
    Sis.listaPersonas.append(A)

def CrearProfesor (Sis):
    P = Profesor
    P.setNombre(input("Ingrese el nombre"))
    P.setApellido(input("Ingrese el apellido"))
    P.setDescuento(input("Ingrese el descuento"))
    Sis.listaPersonas.append(P)

def CrearPlato (Sis):
    PL = Plato()
    PL.setNombre(input("Ingrese nombre"))
    PL.setPrecio(input("Ingrese precio"))
    Sis.bufet.append(PL)

def CrearPedido (Sis):
    PD = Pedido()
    O = input("Fecha Creacion")
    PD.setFechaCreacion(O)
    O = input("Plato")
    PD.setPlato(O)
    O = input("Persona")
    for item in Sis.listaPersonas:
        if item.nombre == O:
            PD.setPersona(item)
    O = input("Hora de Entrega")
    PD.setHoraEntrega(O)

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
                    B = input("Nombre nuevo")
                    item.nombre.setNombre(B)
                if A == "2":
                    B = input("Apellido nuevo")
                    item.nombre.setApellido(B)
                if A == "3":
                    B = input("Division nuva")
                    item.nombre.setDivision(B)

            while item is Profesor and A != "4":
                print("1-Modificar Nombre")
                print("2-Modificar Apellido")
                print("3-Modificar Descuento")
                print("4-Salir")
                A = input()
                if A == "1":
                    B = input("Nombre nuevo")
                    item.setNombre(B)
                if A == "2":
                    B = input("Apellido nuevo")
                    item.setApellido(B)
                if A == "3":
                    B = input("Descuento nuevo")
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
                    B = input("Nombre nuevo")
                    item.setNombre(B)
                if A == "2":
                    B = input("Precio nuevo")
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
                    B = input("FechaCreacion nueva")
                    item.setFechaCreacion(B)
                if A == "2":
                    B = input("Plato nuevo")
                    item.setPlato(B)
                if A == "3":
                    B = input("Persona nueva")
                    for met in sis.listaPersonas:
                        if met == B:
                            item.setPersona = met
                if A == "4":
                    B = input("Hora nueva")
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
    temp = input("Ingrese la persona a borrar")
    for item in Sis.listaPersonas:
        if item.nombre == temp:
            Sis.listaPersonas.remove(item)

def EliminarPedido (Sis):
    O = input("Persona pedido")
    for item in Sis.bufet.listaPedidos:
        if item.nombre == O:
            Sis.bufet.listaPedidos.remove(item)





