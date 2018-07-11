import pymysql

class DB (object):
    __instance = None
    __host = None
    __user = None
    __passwd = None
    __db = None

    def __new__(cls):
        if DB.__instance is None:
            DB.__instance = object.__new__(cls)
        return DB.__instance

    def setConnection(self, host, user, passwd, db):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__db = db

    def run (self, query):
        db = pymysql.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__db, charset='utf8', autocommit=True)
        cursorDB = db.cursor(pymysql.cursors.DictCursor)
        cursorDB.execute(query)

class Persona (object):
    id = None
    nombre = None
    apellido = None

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

    def guardate(self, id):
        if id is "Null":
            self.insertate()
        else:
            self.actualizate()

    def deserializar(self, dict):
        self.nombre = dict["Nombre"]
        self.apellido = dict["Apellido"]

class Autor (Persona):
    generoPrincipal = None


    def setGeneroPrincipal(self, generoPrincipal):
        self.generoPrincipal = generoPrincipal

    def insertate(self):
        DB().run("INSERT INTO Autor VALUES (NULL, '%s', '%s')" %(self.nombre, self.generoPrincipal))

    def actualizate(self):
        DB().run("UPDATE Autor SET Nombre = '%s', Apellido = '%s', GeneroPrincipal = '%s' WHERE idAutor = %i"
                 %(self.nombre, self.apellido, self.generoPrincipal, self.id))

    def eliminate(self):
        DB().run("DELETE FROM Autor WHERE idAutor = %i" %self.id)

    def deserializar(self, dict):
        super().deserlializar(self, dict)
        self.id = dict["idAutor"]
        self.generoPrincipal = dict["GeneroPrincipal"]



class Dueño (Persona):

    def deserializar(self, dict):
        super().deserlializar(self, dict)
        self.id = dict["idDueño"]

    def insertate(self):
        DB().run("INSERT INTO Dueño VALUES (NULL, '%s', '%s');" %(self.nombre, self.apellido))

    def actualizate(self):
        DB().run("UPDATE Dueño SET Nombre = '%s', Apellido = '%s' WHERE idDueño = %i"
                 %(self.nombre, self.apellido, self.id))

    def eliminate(self):
        DB().run("DELETE FROM Dueño WHERE idDueño = %i" %self.id)

class Libro (object):
    idLibro = None
    titulo = None
    cantPaginas = None
    autor = None



    def deserializar(self, dict, autor):
        self.idLibro = dict["idLibro"]
        self.titulo = dict["Titulo"]
        self.cantPaginas = dict["Direccion"]
        self.autor = autor

    def insertate(self):
        DB().run("INSERT INTO Libro VALUES (NULL, '%s', %i, %i)" %(self.titulo, self.cantPaginas, self.autor.idAutor))

    def actualizate(self):
        DB().run("UPDATE Libro SET Titulo = '%s', CantPaginas = %i, Autor = %i WHERE idLibro = %i" %(self.titulo, self.cantPaginas, self.autor.idAutor, self.idLibro))

    def eliminate(self):
        DB().run("DELETE FROM Libro WHERE idLibro = %i" %self.idLibro)

    def guardate(self):
        if self.id is None:
            self.insertate()
        else:
            self.actualizate()

class Libreria (object):
    idLibreria = None
    nombre = None
    direccion = None
    dueño = None

    def __init__(self):
        self.listaLibros = []

    def deserializar(self, dict, dueño, listaLibros):
        self.idLibreria = dict["idLibreria"]
        self.nombre = dict["Nombre"]
        self.direccion = dict["Direccion"]
        self.dueño = dueño
        self.listaLibros = listaLibros

    def insertate(self):
        DB().run("INSERT INTO Libreria VALUES (NULL, '%s', '%s', %i)" %(self.nombre, self.direccion, self.dueño.idDueño))
        for item in self.listaLibros:
            DB().run("INSERT INTO Libreria_has_Libro VALUES (%i, %i)" %(self.idLibreria, item.idLibro))

    def actualizate(self):
        DB().run("UPDATE Libreria SET Nombre = '%s', Direccion = '%s', Dueño = %i WHERE idLibreria = %i" %(self.nombre, self.direccion, self.dueño.idDueño, self.idLibreria))

    def eliminate(self):
        DB().run("DELETE FROM Libreria WHERE idLibreria = %i" %self.idLibreria)

    # def eliminarLibro
    # def añadirLibro