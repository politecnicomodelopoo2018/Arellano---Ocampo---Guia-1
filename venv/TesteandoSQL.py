import pymysql
from DBClass import *
from PersonaClass import *
from LibreriaClass import *
from LibroClass import *
from Funciones import *

DB().setConnection('127.0.0.1','root', 'alumno', 'PruebaLibreria')

d1 = Dueño()
d1 = traerDueño(1)
d1.setNombre("lope")
d1.setApellido("lopez")
d1.guardate()

d1.setNombre("lalalala")
d1.guardate()
a1 = Autor()
a1 = traerAutor(1)
a1.setNombre("cucolo")
a1.setApellido("paralana")
a1.setGeneroPrincipal("rock")
a1.guardate()
a1 = traerAutor(1)

l1 = Libro()
l1 = traerLibro(1)
l1.setTitulo("la caka")
l1.setCantPaginas(22)
l1.setAutor(a1)
l1.guardate()
l1 = traerLibro(1)

lib1 = Libreria()
lib1 = traerLibreria(1)
lib1.setNombre("librin")
lib1.setDireccion("caracas 2334")
lib1.setDueño(d1)
lib1.guardate()
