from Persona import *

def MenuBase():
    print("Menu:")
    print("1- Alumno")
    print("2- Profesor")
    print("3- Platos")
    print("4- Pedidos")
    print("5- Listas")
    print("6- Salir")

def MenuAMEV():
    print("1- Añadir")
    print("2- Modificar")
    print("3- Eliminar")
    print("4- Volver")

def Lista(Sis):
    if len(Sis.bufet.listaPedidos) < 1:
        print("Lista Vacia")
        return
    for item in Sis.bufet.listaPedidos:
        print(item.persona.nombre, (int(item.plato.precio) / 100) * (100-int(item.persona.getDescuento())))

def ListaGente(Sis):
    if len(Sis.listaPersonas) < 1:
        print("Lista Vacia")
        return
    for item in Sis.listaPersonas:
        if type(item) is Alumno:
            print("A|",item.nombre, "|", item.apellido, "|", item.division)
    for item in Sis.listaPersonas:
        if type(item) is Profesor:
            print("P|",item.nombre, "|", item.apellido, "|", item.descuento)

def ListaPlatos(Sis):
    if len(Sis.bufet.listaPlatos) < 1:
        print("Lista Vacia")
        return
    for item in Sis.bufet.listaPlatos:
        print(item.nombre, "|", item.precio)

def SavePlatos(Sis, Archivo):
    f = open(Archivo, "w")








