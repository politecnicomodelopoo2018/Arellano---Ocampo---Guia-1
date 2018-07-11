import pymysql
from Clases import *
from Funciones import *

DB().setConnection('127.0.0.1','root', 'alumno', 'PruebaLibreria')

d1 = Dueño()
d1.setNombre("lope")
d1.setApellido("lopez")
d1.guardate()

a1 = Autor()
a1.setNombre("jemen")
a1.setApellido("gules")
a1.setGeneroPrincipal("rock")
a1.guardate()

