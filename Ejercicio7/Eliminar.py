def EliminarDeListaPersona (Sis):
    temp = input("Ingrese la persona a borrar:")
    for item in Sis.listaPersonas:
        if item.nombre == temp:
            Sis.listaPersonas.remove(item)

def EliminarPedido (Sis):
    temp = input("Persona pedido:")
    for item in Sis.bufet.listaPedidos:
        if item.nombre == temp:
            Sis.bufet.listaPedidos.remove(item)

def EliminarPlato (Sis):
    temp = input("Ingrese el plato a borrar:")
    for item in Sis.bufet.listaPlatos:
        if item.nombre == temp:
            Sis.bufet.listaPlatos.remove(item)