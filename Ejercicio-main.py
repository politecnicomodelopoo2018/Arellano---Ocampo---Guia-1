
from Ejercicio7 import *

menu = True
opcion = 0
opcionB = 0
Sis = Colegio()
temp = None

while menu:
    print("Menu:")
    print("1- Alumno")
    print("2- Profesor")
    print("3- Platos")
    print("4- Pedidos")
    print("5- Salir")

    opcion = input()

    while opcion == 1:
        print("1- Añadir")
        print("2- Modificar")
        print("3- Eliminar")

        opcionB = input()

        if opcionB == 1:
            CrearAlumno(Sis)

        if opcionB == 2:
            print("Ingrese el alumno a modificar")
            temp = input()
            ModificarAlumno(Sis, temp)





    if opcion == 5:
        menu = False
