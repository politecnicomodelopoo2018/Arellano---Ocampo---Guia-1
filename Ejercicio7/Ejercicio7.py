def MenuBase():
    print("Menu:")
    print("1- Alumno")
    print("2- Profesor")
    print("3- Platos")
    print("4- Pedidos")
    print("5- Lista")
    print("6- Salir")

def MenuAMEV():
    print("1- Añadir")
    print("2- Modificar")
    print("3- Eliminar")
    print("4- Volver")

def Lista(Sis):
    for item in Sis.bufet.listaPedidos:
        if type(item.persona) == Profesor:
            print(item.nombre, item.plato.precio*item.persona.descuento)
        else:
            print(item.nombre, item.plato.precio)
    wait = input("Press enter")



