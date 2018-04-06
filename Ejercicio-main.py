
from datetime import date
from PracticaPrueba2 import Persona
from PracticaPrueba2 import Plato
from PracticaPrueba2 import Familia

gabriela = Persona()

gabriela.setNombre("Gabriela")
gabriela.setFechaNac(date(1986, 3, 26))

jorge = Persona()

jorge.setNombre("Jorge")
jorge.setFechaNac(date(2001, 5, 13))

fideos = Plato()
fideos.setNombre("penne")
fideos.setCantCal(500)

combo_mac = Plato()
combo_mac.setNombre("Doble Cuarto de Libra")
combo_mac.setCantCal(827)

churrasco = Plato()
churrasco.setNombre("Dragon Dildo")
churrasco.setCantCal(1000)

morfi = [fideos, fideos, combo_mac, churrasco, combo_mac, churrasco, churrasco, churrasco, churrasco, churrasco]
morfi2 = [fideos]

jorge.setListaPlatos(morfi)
gabriela.setListaPlatos(morfi2)

okeimp = Familia()
okeimp.addIntegrante(jorge)
okeimp.addIntegrante(gabriela)

print(okeimp.getPersonaMin().nombre)
print(okeimp.getPersonaMax().nombre)
print(okeimp.getPromCal())