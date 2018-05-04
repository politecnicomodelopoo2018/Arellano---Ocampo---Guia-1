def CrearAlumno (Sis):
    A = Alumno()
    A.setNombre(input("Ingrese el nombre:"))
    A.setApellido(input("Ingrese el apellido:"))
    A.setDivision(input("Ingrese la division:"))
    Sis.listaPersonas.append(A)

def CrearProfesor (Sis):
    P = Profesor()
    P.setNombre(input("Ingrese el nombre:"))
    P.setApellido(input("Ingrese el apellido:"))
    P.setDescuento(input("Ingrese el descuento:"))
    Sis.listaPersonas.append(P)

def CrearPlato (Sis):
    PL = Plato()
    PL.setNombre(input("Ingrese nombre:"))
    PL.setPrecio(input("Ingrese precio:"))
    Sis.bufet.listaPlatos.append(PL)

def CrearPedido (Sis):
    PD = Pedido()
    O = input("Fecha Creacion:")
    PD.setFechaCreacion(O)
    O = input("Plato")
    for item in Sis.bufet.listaPedidos:
        if item.nombre == O:
            PD.setPlato(item)
    O = input("Persona")
    for item in Sis.listaPersonas:
        if item.nombre == O:
            PD.setPersona(item)
    O = input("Hora de Entrega:")
    PD.setHoraEntrega(O)