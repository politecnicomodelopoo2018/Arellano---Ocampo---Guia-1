from Ejercicio2Alumno import Alumno
from Ejercicio2Materia import  Materia
from calendar import monthrange
from Ejercicio4 import Empresa
from Ejercicio4 import Empleado
import datetime


a = Empleado()

b = Empresa()

a.setApellido("Ocampo")
a.setNombre("Jorge")
a.setFechaNac(datetime.date(2001, 5, 13))
horario = [True, True, True, True, True, False, False]
a.setListaHorario(horario)
asistencias = [datetime.date(2011, 5, 13), datetime.date(2011, 5, 14), datetime.date(2011, 5, 15), datetime.date(2011, 5, 16) , datetime.date(2011, 5, 17), datetime.date(2011, 5, 18), datetime.date(2011, 5, 19),datetime.date(2011, 5, 20), datetime.date(2011, 5, 1)]
a.setListaAsistencia(asistencias)
a.setTelefono(123412141)

b.AgregarEmpleado(a)

print(b.asistenciaMensual(2011,5, "Jorge"))

