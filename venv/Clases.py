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

    def guardate(self):
        if self.id is None:
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
        DB().run("INSERT INTO Autor VALUES (NULL, '%s', '%s', '%s')" %(self.nombre, self.apellido, self.generoPrincipal))

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

    def insertate(self):
        DB().run("INSERT INTO Dueño VALUES (NULL, '%s', '%s');" %(self.nombre, self.apellido))

    def actualizate(self):
        DB().run("UPDATE Dueño SET Nombre = '%s', Apellido = '%s' WHERE idDueño = %i"
                 %(self.nombre, self.apellido, self.id))

    def eliminate(self):
        DB().run("DELETE FROM Dueño WHERE idDueño = %i" %self.id)

    def deserializar(self, dict):
        super().deserlializar(self, dict)
        self.id = dict["idDueño"]
