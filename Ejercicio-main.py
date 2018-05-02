
from Ejercicio7 import *

menu = True
opcion = 0
opcionB = 0
bufet = Bufet()
Sis = Colegio(bufet)
temp = None
while opcion != "5":
    MenuBase()
    opcion = input()

    ##Alumno
    while opcion == "1":
        MenuAMEV()

        opcionB = input()

        if opcionB == "1":
            CrearAlumno(Sis)

        elif opcionB == "2":
            print("Ingrese el alumno a modificar")
            temp = input()
            ModificarPersona(Sis, temp)

        elif opcionB == "3":
            EliminarDeListaPersona(Sis)

        elif opcionB == "4":
            opcion = 0

    ##Profesor
    while opcion == "2":
        MenuAMEV()

        opcionB = input()

        if opcionB == "1":
            CrearProfesor(Sis)

        elif opcionB == "2":
            temp = input("Ingrese el profesor a modificar")
            ModificarPersona(Sis, temp)

        elif opcionB == "3":
            EliminarDeListaPersona(Sis)

        elif opcionB == "4":
            opcion = 0

    ##Platos
    while opcion == "3":
        MenuAMEV()
        opcionB = input()

        if opcion == "1":
            CrearPlato(Sis)

        elif opcionB == "2":
            temp = input("Ingrese el nombre del plato")
            ModificarPlato(Sis, temp)

        elif opcionB == "3":
            EliminarPlato(Sis)

        elif opcionB == "4":
            opcion = 0

    ##Pedidos
    while opcion == "4":
        MenuAMEV()

        opcionB = input()

        if opcion == "1":
            CrearPedido(Sis)

        elif opcionB == "2":
            temp = input("Ingrese la persona del pedido")
            ModificarPedido(Sis, temp)

        elif opcionB == "3":
            EliminarPedido(Sis)

        elif opcionB == "4":
            opcion = 0





