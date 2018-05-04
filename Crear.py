from Persona import *
from Plato import *
from Pedido import *
import datetime

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


    O = input("Plato")
    for item in Sis.bufet.listaPlatos:
        if item.nombre == O:
            print("Encontre ", item.nombre)
            PD.setPlato(item)
            break
    if not PD.plato:
        print("No existe")
        return

    O = input("Persona")
    for item in Sis.listaPersonas:
        if item.nombre == O:
            print("Encontre ", item.nombre)
            PD.setPersona(item)
            break
    if not PD.persona:
        print("No existe")
        return

    O = input("Fecha Creacion:")
    PD.setFechaCreacion(datetime.datetime.strptime(O, "%Y%m%d"))

    O = input("Hora de Entrega:")
    PD.setHoraEntrega(O)

    Sis.bufet.listaPedidos.append(PD)