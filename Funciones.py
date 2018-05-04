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

## Corregir esto

def Lista(Sis):
    for item in Sis.bufet.listaPedidos:
        print(item.persona.nombre, item.plato.precio * (100-int(item.persona.getDescuento())))




