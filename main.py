#Importacion de librerias
import psycopg2
from flask import Flask, render_template, request, redirect, url_for
#from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

#Creamos un objeto de tipo flask
app = Flask(__name__, static_url_path='/static')
db = SQLAlchemy()
conn = psycopg2.connect(
    host='ec2-52-5-1-20.compute-1.amazonaws.com',
    database='dn808n9aep0cc',
    user='socofjiybjcuyg',
    password='5a5bb7314d8e8e3cc2e2c61be4540453130c33e326ec6a4c5e95e5ce1d48b9f3'
)
#Conexion con MYSQL
#mysql = MySQL()
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = '12345a'
#app.config['MYSQL_DATABASE_DB'] = 'Productos1'
#app.config['MYSQL_DATABASE_PORT'] = 3306

#pip install cryptography
#pip install PYMYSQL[rsa]

#mysql.init_app(app)
app = Flask(__name__, static_url_path='/static')
#Creacion de una ruta raiz a pagina principal
@app.route("/")
#Creamos funciones para llamar el index(pagina principal)
def index():
    return render_template("index.html")
@app.route("/rejilla")
def rejillas_html():
    return render_template("html_rejilla.html")

@app.route("/Bootstrap")
def Bootstrap_html():
    return render_template("Bootstrap.html")

@app.route("/Formulario")
def Formulario():

    #conn = mysql.connect()
    connectar = conn.cursor()

    connectar.execute("select * from productos")

    datos = connectar.fetchall()

    print(datos)
    connectar.close()

    return render_template("Formulario.html", productos=datos)

@app.route("/Guardar_producto", methods=["POST"])
def Guardar_producto():
     Nombre = request.form["Nombre"]
     Precio = request.form["Precio"]
     Descripcion = request.form["Descripcion"]

     #abrimos conexion

     #crear una interacion a la conexion a la bd
     connectar = conn.cursor()

     connectar.execute("INSERT INTO productos(Nombre, Precio, Descripcion) VALUES (%s,%s,%s)",
                       (Nombre, Precio, Descripcion))
     #Actualizar la conexion
     conn.commit()
     #Cerramos la interacion y limpia la conexion para que quede vacia
     connectar.close()

     #return "Dato insertado"+nombre+" "+Precio+" "+description

     return redirect("/Formulario")

     #configuracion de archivo principal de ejecución.

@app.route("/eliminar_producto/<string:IDproducto>")
def eliminar_producto(IDproducto):

    connectar = conn.cursor()

    connectar.execute("Delete from productos where IDproducto={0}".format(IDproducto))
    conn.commit()
    connectar.close()

    #return "Dato eliminado "+id
    return redirect("/Formulario")

@app.route("/consultar_producto/<IDproducto>")
def obtener_producto(IDproducto):

    connectar = conn.cursor()

    connectar.execute("Select * From productos where IDproducto= %s", (IDproducto))
    dato = connectar.fetchone()
    print(dato)
    connectar.close()
    return render_template("form_editar_producto.html", producto=dato)

@app.route("/editar_producto/<IDproducto>", methods=['POST'])
def editar_producto(IDproducto):
    Nombre = request.form["Nombre"]
    Precio = request.form["Precio"]
    Descripcion = request.form["Descripcion"]


    connectar = conn.cursor()
    connectar.execute("UPDATE productos SET Nombre=%s, Precio=%s, Descripcion=%s WHERE IDproducto=%s", (Nombre, Precio, Descripcion, IDproducto))
    conn.commit()
    connectar.close()

    return redirect("/Formulario")

if __name__ == '__main__':
#configurando el puerto de escucha del servicio web
 app.run(port = 3000, debug = True)



