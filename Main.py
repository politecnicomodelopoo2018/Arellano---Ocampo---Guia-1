from Funciones import *
from Radio import *

Radio = Radio()

while opcion != "5":
    Menu()
    opcion = input()

    # Crear Persona
    while opcion == "1":
        Radio.listaGente.append(CrearPersona())

    # Crear Programa
    while opcion == "2":
        CrearPrograma(categoria)

    # Guardar
    elif opcion == "3":
        Guardar()

    # Cargar
    elif opcion == "4":
        Cargar()
