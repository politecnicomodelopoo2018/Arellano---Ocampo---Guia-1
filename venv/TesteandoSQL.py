import pymysql
import Clases









DB().setConnection("127.0.0.1", "root", "alumno", "PruebaLibreria")
DB().run("INSERT INTO Autor VALUES (NULL, 'Nacho', 'Cienca Ficcion')")