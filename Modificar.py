from Persona import *

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
                    B = input("Nombre nuevo:")
                    item.setNombre(B)
                if A == "2":
                    B = input("Apellido nuevo:")
                    item.setApellido(B)
                if A == "3":
                    B = input("Division nueva:")
                    item.setDivision(B)

            while type(item) is Profesor and A != "4":
                print("1-Modificar Nombre")
                print("2-Modificar Apellido")
                print("3-Modificar Descuento")
                print("4-Salir")
                A = input()
                if A == "1":
                    B = input("Nombre nuevo:")
                    item.setNombre(B)
                if A == "2":
                    B = input("Apellido nuevo:")
                    item.setApellido(B)
                if A == "3":
                    B = input("Descuento nuevo:")
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
                    B = input("Nombre nuevo:")
                    item.setNombre(B)
                if A == "2":
                    B = input("Precio nuevo:")
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
                    B = input("FechaCreacion nueva:")
                    item.setFechaCreacion(B)
                if A == "2":
                    B = input("Plato nuevo:")
                    item.setPlato(B)
                if A =="3":
                    B = input("Persona nueva:")
                    for met in sis.listaPersonas:
                        if met == B:
                            item.setPersona = met
                if A == "4":
                    B = input("Hora nueva:")
                    item.setHoraEntrega(B)
                if A == "5":
                    print("1-Entregado")
                    print("2-No entregado")
                    B = input()
                    if B == "1":
                        item.setEntregado(True)
                    if B == "2":
                        item.setEntregado(False)