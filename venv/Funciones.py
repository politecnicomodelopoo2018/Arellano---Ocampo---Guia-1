import pymysql
from DBClass import *
from PersonaClass import *
from LibreriaClass import *
from LibroClass import *
from Funciones import *

def traerAutor(id):
    autor = Autor()
    cur = DB().run("SELECT * FROM Autor WHERE idAutor = %i" %id)
    dict = cur.fetchone()
    autor.deserializar(dict)
    return autor

def traerDueño(id):
    dueño = Dueño()
    cur = DB().run("SELECT * FROM Dueño WHERE idDueño = %i" %id)
    dict = cur.fetchone()
    dueño.deserializar(dict)
    return dueño

def traerLibro(id):
    libro = Libro()
    cur = DB().run("SELECT * FROM Libro WHERE idLibro = %i" %id)
    dict = cur.fetchone()
    autor = traerAutor(dict["Autor_idAutor"])
    libro.deserializar(dict, autor)
    return libro

def traerLibreria(id):
    libreria = Libreria()
    cur = DB().run("SELECT * FROM Libreria WHERE idLibreria = %i" %id)
    dict = cur.fetchone()
    dueño = traerDueño(dict["Dueño_idDueño"])
    libreria.deserializar(dict, dueño)
    return libreria

