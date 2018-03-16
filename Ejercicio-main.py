from Ejercicio2Alumno import Alumno
from Ejercicio2Materia import  Materia
import datetime


a = Alumno()
a.setNombre("Jorge")
a.setApellido("Lucas")
fecha = datetime.date(2000, 12, 31)
a.setFecha_de_nac(fecha)

a.agregarMateria("Matematica")
a.agregarMateria("Lengua")
a.agregarMateria("Civica")

print("monja")

a.agregarNota(1, "Matematica")
a.agregarNota(7, "Matematica")
a.agregarNota(2, "Civica")
a.agregarNota(8, "Civica")

print("atroden")

print(a.promedioNotasMateria("Matematica"))
print(a.promedio())
