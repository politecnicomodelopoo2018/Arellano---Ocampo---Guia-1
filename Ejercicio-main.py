
from Ejercicio7 import *

menu = True
opcion = 0
opcionB = 0
bufet = Bufet()
Sis = Colegio(bufet)
temp = None
while opcion != "5":
    print("Menu:")
    print("1- Alumno")
    print("2- Profesor")
    print("3- Platos")
    print("4- Pedidos")
    print("5- Salir")

    opcion = input()

    while opcion == "1":
        print("1- Añadir")
        print("2- Modificar")
        print("3- Eliminar")
        print("4- Volver")

        opcionB = input()

        if opcionB == "1":
            CrearAlumno(Sis)

        if opcionB == "2":
            print("Ingrese el alumno a modificar")
            temp = input()
            ModificarPersona(Sis, temp)

        if opcionB == "3":
            EliminarDeListaPersona(Sis)

        if opcionB == "4":
            opcion = 0

    while opcion == "2":
        print("1- Añadir")
        print("2- Modificar")
        print("3- Eliminar")
        print("4- Volver")

        opcionB = input()

        if opcionB == "1":
            CrearProfesor(Sis)

        if opcionB == "2":
            print("Ingrese el profesor a modificar")
            temp = input()
            ModificarPersona(Sis, temp)

        if opcionB == "3":
            EliminarDeListaPersona(Sis)

        if opcionB == "4":
            opcion = 0




