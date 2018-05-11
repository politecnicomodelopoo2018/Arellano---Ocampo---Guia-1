from Ejercicio7.Persona import *
from Ejercicio7.Plato import *

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
            print("Alumno-",item.nombre, "-", item.apellido, "-", item.division)
    for item in Sis.listaPersonas:
        if type(item) is Profesor:
            print("Profesor-",item.nombre, "-", item.apellido, "-", item.descuento)

def ListaPlatos(Sis):
    if len(Sis.bufet.listaPlatos) < 1:
        print("Lista Vacia")
        return
    for item in Sis.bufet.listaPlatos:
        print(item.nombre, "-", item.precio)

def getPersonaFromArchive(line):
    datos = line.split("|")
    x=eval(datos[0])()
    x.loadFromString(datos)
    return x

def getPlatoFromArchive(line):
    pl = Plato()
    datos = line.split("|")
    pl.setNombre(datos[0])
    pl.setPrecio(datos[1])
    return pl

def SavePlato(archivo, sis):
    with open(archivo, "w") as f:
        for item in sis.bufet.listaPlatos:
            f.write(item.pasarGuardar)

def ChargePlato(sis, archivo):
    with open(archivo, "r") as f:
        for line in f:
            sis.bufet.listaPlatos.append(getPlatoFromArchive(line))

def SaveGente(archivo, sis):
    with open(archivo, "w") as f:
        for item in sis.listaPersonas:
            f.write(item.pasarGuardar())

def ChargePersonas(sis, archivo):
    with open(archivo, "r") as f:
        for line in f:
            sis.listaPersonas.append(getPersonaFromArchive(line))










