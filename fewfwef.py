import json
import datetime

def recuperarPersona(valor):
    P = Persona(valor["nombre"], valor["apellido"], valor["fechaNac"])
    return P

class Persona (object):

    def __init__(self, nombre, apellido, fechaNac):
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNac = fechaNac



P1 = Persona("Luis", "Gomez", datetime(2000, 10, 25))
P2 = Persona("Jorge", "Ocampo", datetime(2001, 9, 3))
P3 = Persona("Juan", "Luisñ", datetime(2000, 5, 3))

ListaPersonas = [P1, P2, P3]

with open("hola.txt", "r") as f:
    esto = json.load(f)

d = esto

for item in d["personas"]:
    ListaPersonas.append(recuperarPersona(item))

print(d["personas"][0])




d = {"personas": []}

for item in ListaPersonas:
    d["personas"].append(item.__dict__)



with open("hola.txt", "w") as f:
    for item in d["personas"]:
        f.write(json.dumps(d, ensure_ascii=False, indent=4))


