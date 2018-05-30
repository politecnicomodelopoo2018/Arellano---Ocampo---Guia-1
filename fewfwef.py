import json
from datetime import *

def recuperarPersona(valor):
    P = Persona(valor["nombre"], valor["apellido"], valor["fechaNac"])
    return P

class Persona (object):

    def __init__(self, nombre, apellido, fechaNac):
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNac = fechaNac

    def serlizar(self):
        d = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fechaNac": (str(self.fechaNac.year) + "/" + str(self.fechaNac.month) + "/" + str(self.fechaNac.day))
        }
        return d

    def descerializar(self, dict):
        self.nombre = dict["nombre"]
        self.apellido = dict["apellido"]
        self.fechaNac = datetime.strptime(dict["fechaNac"], "%Y/%m/%d")

P1 = Persona("Luis", "Gomez", datetime(2000, 10, 25))
P2 = Persona("Jorge", "Ocaño", datetime(2001, 9, 3))
P3 = Persona("Juan", "Luisñ", datetime(2000, 5, 3))

ListaPersonas = [P1, P2, P3]

d = d = {"persona": []}


for item in ListaPersonas:
    d["persona"].append(item.serlizar())

with open("hola.json", "w") as f:
    f.write(json.dumps(d, ensure_ascii= False, indent=4))

with open("hola.json", "r") as f:
    d = json.loads(f.read())

for item in d["persona"]:
    unaPersona = Persona(None, None, None)
    unaPersona.descerializar(item)
    ListaPersonas.append(unaPersona)
