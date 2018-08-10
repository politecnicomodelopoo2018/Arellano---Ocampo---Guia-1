import pymysql
from DBClass import *

class Persona (object):
    id = None
    nombre = None

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def insertate(self):
        pass

    def actualizate(self):
        pass

    def guardate(self):
        if self.id is None:
            self.insertate()
        else:
            self.actualizate()

    def deserializar(self, dict):
        self.nombre = dict["Nombre"]

class Autor (Persona):
    generoPrincipal = None


    def setGeneroPrincipal(self, generoPrincipal):
        self.generoPrincipal = generoPrincipal

    def insertate(self):
        cur = DB().run("INSERT INTO Autor VALUES (NULL, '%s', '%s')" %(self.nombre, self.generoPrincipal))
        self.id = cur.lastrowid

    def actualizate(self):
        DB().run("UPDATE Autor SET Nombre = '%s', GeneroPrincipal = '%s' WHERE idAutor = %i"
                 %(self.nombre, self.generoPrincipal, self.id))

    def eliminate(self):
        DB().run("DELETE FROM Autor WHERE idAutor = %i" %self.id)


    def deserializar(self, dict):
        super().deserializar(dict)
        self.id = dict["idAutor"]
        self.generoPrincipal = dict["GeneroPrincipal"]

    @staticmethod
    def traerAutor(id):
        autor = Autor()
        cur = DB().run("SELECT * FROM Autor WHERE idAutor = %i" % id)
        dict = cur.fetchone()
        autor.deserializar(dict)
        return autor

    @staticmethod
    def getAllAutores():
        cur = DB().run("SELECT idAutor FROM Autor")
        listaDict = cur.fetchall()
        listaAutores = []
        for item in listaDict:
            listaAutores.append(Autor.traerAutor(item["idAutor"]))
        return listaAutores


class Dueño (Persona):
    apellido = None

    def deserializar(self, dict):
        super().deserializar(dict)
        self.apellido = dict["Apellido"]
        self.id = dict["idDueño"]

    def insertate(self):
        cur = DB().run("INSERT INTO Dueño VALUES (NULL, '%s', '%s');" %(self.nombre, self.apellido))
        self.id = cur.lastrowid


    def actualizate(self):
        DB().run("UPDATE Dueño SET Nombre = '%s', Apellido = '%s' WHERE idDueño = %i"
                 %(self.nombre, self.apellido, self.id))

    def eliminate(self):
        DB().run("DELETE FROM Dueño WHERE idDueño = %i" %self.id)

    @staticmethod
    def traerDueño(id):
        dueño = Dueño()
        cur = DB().run("SELECT * FROM Dueño WHERE idDueño = %i" % id)
        dict = cur.fetchone()
        dueño.deserializar(dict)
        return dueño

    @staticmethod
    def getAllDueños():
        cur = DB().run("SELECT idDueño FROM Dueño")
        listaDict = cur.fetchall()
        listaDueños = []
        for item in listaDict:
            listaDueños.append(Dueño.traerDueño(item["idDueño"]))
        return listaDueños
