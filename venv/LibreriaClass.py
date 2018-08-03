import pymysql
from DBClass import *

class Libreria (object):
    idLibreria = None
    nombre = None
    direccion = None
    dueño = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setDueño(self, dueño):
        self.dueño = dueño

    def setListaLibros(self, listaLibros):
        self.listaLibros = listaLibros

    def addLibro(self, libro):
        DB().run("INSERT INTO Libreria_has_Libro VALUES(%i, %i)" %(self.idLibreria, libro.idLibro))

    def removeLibro(self, libro):
        DB().run("DELETE FROM Libreria_has_Libro WHERE Libro_idLibro = %i" %libro.idLibro)

    def deserializar(self, dict, dueño):
        self.idLibreria = dict["idLibreria"]
        self.nombre = dict["Nombre"]
        self.direccion = dict["Direccion"]
        self.dueño = dueño

    def getListaLibros(self):
        cur = DB().run("SELECT Libro_idLibro FROM Libreria_has_Libro WHERE Libreria_idLibreria = %i" %idLibreria)
        lista = cur.fetchall()
        for item in lista:
            listaLibro.append(traerLibro(item))
        return listaLibro

    def insertate(self):
        cur = DB().run("INSERT INTO Libreria VALUES (NULL, '%s', '%s', %i)" %(self.nombre, self.direccion, self.dueño.id))
        self.idLibreria = cur.lastrowid

    def actualizate(self):
        DB().run("UPDATE Libreria SET Nombre = '%s', Direccion = '%s', Dueño_idDueño = %i WHERE idLibreria = %i" %(self.nombre, self.direccion, self.dueño.id, self.idLibreria))

    def eliminate(self):
        DB().run("DELETE FROM Libreria WHERE idLibreria = %i" %self.idLibreria)

    def guardate(self):
        if self.idLibreria is None:
            self.insertate()
        else:
            self.actualizate()