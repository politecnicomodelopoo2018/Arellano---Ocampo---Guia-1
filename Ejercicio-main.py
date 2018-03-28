from Ejercicio3 import Jugador
from Ejercicio3 import Equipo
from Ejercicio3 import Torneo
from Ejercicio3 import Partido
from Ejercicio3 import Dia
from datetime import date

jorge = Jugador()

jorge.setNombre("Jorge")
jorge.setFechaNac(datetime.date(2001,5,13))
jorge.setCapitanState(True)
jorge.setNCamiseta(10)

lunes = Dia()
lunes.setTurno([True, True, True])
martes = Dia()
martes.setTurno([True, True, True])
miercoles = Dia()
miercoles.setTurno([True, True, True])
jueves = Dia()
jueves.setTurno([True, True, True])
viernes = Dia()
viernes.setTurno([True, True, True])
sabado = Dia()
sabado.setTurno([True, True, True])
chanchos = Equipo()

chanchos.setNombre("Los Chanchos")
chanchos.setBarrio("Flores")
chanchos.setListaHorarios()

