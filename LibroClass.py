import pymysql
from DBClass import *
from PersonaClass import *

class Libro (object):
    idLibro = None
    titulo = None
    cantPaginas = None
    autor = None

    def setIdLibro(self, idLibro):
        self.idLibro = idLibro

    def setTitulo (self, titulo):
        self.titulo = titulo

    def setCantPaginas(self, cantPaginas):
        self.cantPaginas = cantPaginas

    def setAutor(self, autor):
        self.autor = autor

    def deserializar(self, dict, autor):
        self.idLibro = dict["idLibro"]
        self.titulo = dict["Titulo"]
        self.cantPaginas = dict["CantPaginas"]
        self.autor = autor

    def insertate(self):
        cur = DB().run("INSERT INTO Libro VALUES (NULL, '%s', %i, %i)" %(self.titulo, self.cantPaginas, self.autor.id))
        self.idLibro = cur.lastrowid

    def actualizate(self):
        DB().run("UPDATE Libro SET Titulo = '%s', CantPaginas = %i, Autor_idAutor = %i WHERE idLibro = %i" %(self.titulo, self.cantPaginas, self.autor.id, self.idLibro))

    def eliminate(self):
        DB().run("DELETE FROM Libro WHERE idLibro = %i" %self.idLibro)

    def guardate(self):
        if self.idLibro is None:
            self.insertate()
        else:
            self.actualizate()

    @staticmethod
    def traerLibro(id):
        libro = Libro()
        cur = DB().run("SELECT * FROM Libro WHERE idLibro = %i" % id)
        dict = cur.fetchone()
        autor = Autor.traerAutor(dict["Autor_idAutor"])
        libro.deserializar(dict, autor)
        return libro

    @staticmethod
    def getAllLibros():
        cur = DB().run("SELECT idLibro FROM Libro")
        listaDict = cur.fetchall()
        listaLibros = []
        for item in listaDict:
            listaLibros.append(Libro.traerLibro(item["idLibro"]))
        return listaLibros