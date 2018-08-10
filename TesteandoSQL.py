import pymysql
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from DBClass import *
from PersonaClass import *
from LibreriaClass import *
from LibroClass import *

DB().setConnection('127.0.0.1','root', 'alumno', 'PruebaLibreria')

app = Flask(__name__, static_url_path='/static')


lista = Libro.getAllLibros()

for item in lista:
    print(item.cantPaginas)

@app.route('/')
def Index():
    return redirect("/paginaPrincipal")


@app.route('/paginaPrincipal')
def PaginaPrincipal():
    return render_template("paginaPrincipal.html")


@app.route('/abmDueño')
def AbmDueño():
    return render_template("abmDueño.html",  ListaDueños=Dueño.getAllDueños())

@app.route('/abmAutor')
def AbmAutor():
    return render_template("abmAutor.html",  ListaAutores=Autor.getAllAutores())

@app.route('/abmLibro')
def AbmLibro():
    return render_template("abmLibro.html", ListaLibros=Libro.getAllLibros())

@app.route('/abmLibreria')
def AbmLibreria():
    return render_template("abmLibreria.html", ListaLibrerias=Libreria.getAllLibrerias())

@app.route('/libros')
def AbmLibros():
    return render_template("libros.html", ListaLibros=Libreria.traerLibreria(int(request.args.get("idLibreria"))).getListaLibros(), Libreria=Libreria.traerLibreria(int(request.args.get("idLibreria"))))

@app.route('/bajaAutor')
def BajaAutor():
    autor = Autor.traerAutor(int(request.args.get("idAutor")))
    autor.eliminate()
    return render_template("abmAutor.html", ListaAutores=Autor.getAllAutores())

@app.route('/bajaDueño')
def BajaDueño():
    dueño = Dueño.traerDueño(int(request.args.get("idDueño")))
    dueño.eliminate()
    return render_template("abmDueño.html", ListaDueños=Dueño.getAllDueños())

@app.route('/bajaLibro')
def BajaLibro():
    libro = Libro.traerLibro(int(request.args.get("idLibro")))
    libro.eliminate()
    return render_template("abmLibro.html", ListaLibros=Libro.getAllLibros())

@app.route('/bajaLibreria')
def BajaLibreria():
    libreria = Libreria.traerLibreria(int(request.args.get("idLibreria")))
    libreria.eliminate()
    return render_template("abmLibreria.html", ListaLibrerias=Libreria.getAllLibrerias())

@app.route('/altaDueño')
def AltaDueño():
    return render_template("altaDueño.html")

@app.route('/insertarDueño', methods=['GET', 'POST'])
def InsertarDueño():
    dueño = Dueño()
    dueño.setNombre(request.form.get("nombre"))
    dueño.setApellido(request.form.get("apellido"))
    dueño.insertate()
    return render_template("abmDueño.html", ListaDueños=Dueño.getAllDueños())

@app.route('/altaAutor')
def AltaAutor():
    return render_template("altaAutor.html")

@app.route('/insertarAutor', methods=['GET', 'POST'])
def InsertarAutor():
    autor = Autor()
    autor.setNombre(request.form.get("nombre"))
    autor.setGeneroPrincipal(request.form.get("generoPrincipal"))
    autor.insertate()
    return render_template("abmAutor.html", ListaAutores=Autor.getAllAutores())

@app.route('/altaLibro')
def AltaLibro():
    return render_template("altaLibro.html", ListaAutores=Autor.getAllAutores())

@app.route('/insertarLibro', methods=['GET', 'POST'])
def InsertarLibro():
    libro = Libro()
    libro.setTitulo(request.form.get("titulo"))
    libro.setCantPaginas(int(request.form.get("cantPaginas")))
    libro.setAutor(Autor.traerAutor(int(request.form.get("idAutor"))))
    libro.insertate()
    return render_template("abmLibro.html", ListaLibros=Libro.getAllLibros())

@app.route('/altaLibreria')
def AltaLibreria():
    return render_template("altaLibreria.html", ListaDueños=Dueño.getAllDueños())

@app.route('/insertarLibreria', methods=['GET', 'POST'])
def InsertarLibreria():
    libreria = Libreria()
    libreria.setNombre(request.form.get("nombre"))
    libreria.setDireccion(request.form.get("direccion"))
    libreria.setDueño(Dueño.traerDueño(int(request.form.get("idDueño"))))
    libreria.insertate()
    return render_template("abmLibreria.html", ListaLibrerias=Libreria.getAllLibrerias())

@app.route('/removerLibro')
def RemoverLibro():
    libreria = Libreria.traerLibreria(int(request.args.get("idLibreria")))
    libreria.removeLibro(Libro.traerLibro(int(request.args.get("idLibro"))))
    return render_template("libros.html", ListaLibros=libreria.getListaLibros(), Libreria=libreria)

@app.route('/seleccionarLibros')
def SeleccionarLibros():
    return render_template("seleccionarLibros.html", ListaLibros=Libro.getAllLibros(), Libreria=Libreria.traerLibreria(int(request.args.get("idLibreria"))))

@app.route('/añadirLibro', methods=['GET', 'POST'])
def AñadirLibro():
    libro = Libro.traerLibro(int(request.form.get("libro")))
    libreria = Libreria.traerLibreria((int(request.form.get("idLibreria"))))
    libreria.addLibro(libro)
    return render_template("libros.html", ListaLibros=Libreria.traerLibreria(int(request.form.get("idLibreria"))).getListaLibros(), Libreria=libreria)

@app.route('/modificacionDueño')
def ModificacionDueño():
    return render_template("modificacionDueño.html", Dueño=Dueño.traerDueño(int(request.args.get("idDueño"))))

@app.route('/modificarDueño', methods=['GET', 'POST'])
def ModificarDueño():
    dueño = Dueño()
    dueño.setId(int(request.form.get("idDueño")))
    dueño.setNombre(request.form.get("nombre"))
    dueño.setApellido(request.form.get("apellido"))
    dueño.guardate()
    return render_template("abmDueño.html", ListaDueños=Dueño.getAllDueños())

@app.route('/modificacionAutor')
def ModificacionAutor():
    return render_template("modificacionAutor.html", Autor=Autor.traerAutor(int(request.args.get("idAutor"))))

@app.route('/modificarAutor', methods=['GET', 'POST'])
def ModificarAutor():
    autor = Autor()
    autor.setId(int(request.form.get("idAutor")))
    autor.setNombre(request.form.get("nombre"))
    autor.setGeneroPrincipal(request.form.get("generoPrincipal"))
    autor.guardate()
    return render_template("abmAutor.html", ListaAutores=Autor.getAllAutores())

@app.route('/modificacionLibro')
def ModificacionLibro():
    return render_template("modificacionLibro.html", ListaAutores=Autor.getAllAutores(), Libro=Libro.traerLibro(int(request.args.get("idLibro"))))

@app.route('/modificarLibro', methods=['GET', 'POST'])
def ModificarLibro():
    libro = Libro
    libro.setIdLibro(int(request.form.get("idLibro")))
    libro.setTitulo(request.form.get("titulo"))
    libro.setCantPaginas(int(request.form.get("cantPaginas")))
    libro.setAutor(Autor.traerAutor(request.form.get("idAutor")))
    libro.guardate()
    return render_template("abmLibro.html", ListaLibros=Libro.getAllLibros())

if __name__ == '__main__':  # para actualizar automaticamente la pagina sin tener que cerrarla
    app.run(debug=True) # para correr la pagina se puede hacer en este caso "python3 PruebaFlask.py" en la terminal

