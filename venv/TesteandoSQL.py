import pymysql
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from DBClass import *
from PersonaClass import *
from LibreriaClass import *
from LibroClass import *
from Funciones import *

DB().setConnection('127.0.0.1','root', 'alumno', 'PruebaLibreria')

app = Flask(__name__, static_url_path='/static')


lista = getAllLibros()

for item in lista:
    print(item.cantPaginas)

@app.route('/')
def Index():
    return redirect("/paginaPrincipal.html")


@app.route('/paginaPrincipal.html')
def PaginaPrincipal():
    return render_template("paginaPrincipal.html")


@app.route('/abmDueño')
def AbmDueño():
    return render_template("abmDueño.html",  ListaDueños=getAllDueños())

@app.route('/abmAutor')
def AbmAutor():
    return render_template("abmAutor.html",  ListaAutores=getAllAutores())

@app.route('/abmLibro')
def AbmLibro():
    return render_template("abmLibro.html", ListaLibros=getAllLibros())

@app.route('/abmLibreria')
def AbmLibreria():
    return render_template("abmLibreria.html", ListaLibrerias=getAllLibrerias())

@app.route('/libros')
def AbmLibros():
    return render_template("libros.html", ListaLibros=traerLibreria(int(request.args.get("idLibreria"))).getListaLibros())




if __name__ == '__main__':  # para actualizar automaticamente la pagina sin tener que cerrarla
    app.run(debug=True) # para correr la pagina se puede hacer en este caso "python3 PruebaFlask.py" en la terminal

