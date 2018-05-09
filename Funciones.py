from Persona import *
from Plato import *

def MenuBase():
    print("Menu:")
    print("1- Alumno")
    print("2- Profesor")
    print("3- Platos")
    print("4- Pedidos")
    print("5- Listas")
    print("6- Guardar")
    print("7- Cargar")
    print("8- Salir")

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

def getPersonaFromArchive(archivo):
    a = Alumno()
    p = Profesor()
    with open(archivo, "r") as f:
        for line in f:
            datos = line.split("|")
            if datos[0] == "a":
                a.setNombre(datos[1])
                a.setApellido(datos[2])
                a.setDivision(datos[3])
                return a
            else:
                p.setNombre(datos[1])
                p.setApellido(datos[2])
                p.setDescuento(datos[3])
                return p

def getPlatoFromArchive(archivo):
    pl = Plato()
    with open(archivo, "r") as f:
        for line in f:
            datos = line.split("|")
            pl.setNombre(datos[0])
            pl.setPrecio(datos[1])
            return pl

def LoadPersona(persona, sis):
    sis.listaPersonas.append(persona)

def LoadPlato(plato, sis):
    sis.bufet.listaPlatos.append(plato)

def SaveGente(archivo, sis):
    print(sis.listaPersonas[0].pasarGuardar())
    with open(archivo, "w") as f:
        for item in sis.listaPersonas:
            f.write(item.pasarGuardar())










