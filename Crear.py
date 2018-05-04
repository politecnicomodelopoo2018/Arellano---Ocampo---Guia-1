from Persona import *
from Plato import *
from Pedido import *

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
    print("Cargando ", O)
    PD.setFechaCreacion(O)
    O = input("Plato")
    print("Cargando ", O)
    for item in Sis.bufet.listaPlatos:
        if item.nombre == O:
            print("Encontre ", item.nombre)
            PD.setPlato(item)
    O = input("Persona")
    print("Cargando ", O)
    for item in Sis.listaPersonas:
        if item.nombre == O:
            print("Encontre ", item.nombre)
            PD.setPersona(item)
    O = input("Hora de Entrega:")
    print("Cargando ", O)
    PD.setHoraEntrega(O)
    Sis.bufet.listaPedidos.append(PD)