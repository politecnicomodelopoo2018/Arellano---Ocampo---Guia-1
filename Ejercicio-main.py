from Ejercicio2Alumno import Alumno
from Ejercicio2Materia import  Materia
from Ejercicio4 import Empresa
from Ejercicio4 import Empleado

import datetime
from calendar import monthrange

a = Empleado()

b = Empresa(a)

print(b.asistenciaMensual(2011, 10, "Jorge"))