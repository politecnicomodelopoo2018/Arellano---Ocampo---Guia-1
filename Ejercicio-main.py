from Ejercicio1 import Alumno
import datetime


a = Alumno()
a.setNombre("Jorge")
a.setApellido("Lucas")
fecha = datetime.date(2000, 12, 31)
a.setFecha_de_nac(fecha)
a.agregarNota(8)


diferencia = ((datetime.date.today() - a.fecha_de_nac).days / 365.25)

print(int(diferencia))

