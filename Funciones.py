from Persona import *
from Programa import *

def Menu():
    print("1. Crear Persona")
    print("2. Crear Programa")
    print("3. Guardar")
    print("4. Cargar")
    print("5. Salir")

def CrearConductor():
    C = Conductor()
    C.setDni(input("DNI"))
    C.setApellido(input("Apellido"))
    C.setNombre(input("Nombre"))
    C.setFechaIngreso("Fecha")
    return C

def CrearOpTecnico():
    OP = OpTecnico()
    OP.setDni(input("DNI"))
    OP.setApellido(input("Apellido"))
    OP.setNombre(input("Nombre"))
    OP.setFechaIngreso("Fecha")
    return OP

def CrearMusicalizador():
    M = Musicalizador()
    M.setDni(input("DNI"))
    M.setApellido(input("Apellido"))
    M.setNombre(input("Nombre"))
    M.setFechaIngreso("Fecha")
    return M

def CrearPersona():
    while X != 4:
        print("1.Conductor")
        print("2.OpTecnico")
        print("3.Musicalizador")
        print("4.Volver")
        X = int(input())
        if X == 1:
            return CrearConductor()
        elif X == 2:
            return CrearOpTecnico()
        elif X == 3:
            return CrearMusicalizador()

def CrearPrograma(categoria):
    if categoria != "musica":
        P = ProgramaMusica()
        P.setNombre(input("Nombre"))
        P.setCategoria(categoria)
        P.setMusicalizador()


    P.setNombre(input("Nombre"))



