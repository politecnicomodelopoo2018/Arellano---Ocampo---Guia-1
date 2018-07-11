import pymysql
from Clases import *

def traerAutor(id):
    autor = Autor()
    dict = DB().run("SELECT * FROM Autor WHERE idAutor = %i" %id)
    autor.deserializar(dict)
    return autor

def traerDueño(id):
    dueño = Dueño()
    dict = DB().run("SELECT * FROM Dueño WHERE idDueño = %i" %id)
    dueño.deserializar(dict)
    return dueño

def traerLibro(id):
    libro = Libro()
    dict = DB().run("SELECT * FROM Libro WHERE idLibro = %i" %id)
    autor = traerAutor(dict["Autor_idAutor"])
    libro.deserializar(dict, autor)
    return libro

def traerLibreria(id):
    libreria = Libreria()
    dict = DB().run("SELECT * FROM Libreria WHERE idLibreria = %%i" %id)
    dueño = traerDueño(dict["Dueño_idDueño"])
    libreria.deserializar(dict, dueño)
    return libreria