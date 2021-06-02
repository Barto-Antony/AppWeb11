#Importacion de librerias
from flask import Flask,render_template
#Creamos un objeto de tipo flask
app = Flask(__name__)
#Creacion de una ruta raiz a pagina principal
@app.route("/")
#Creamos funciones para llamar el index(pagina principal)
def index():

    return render_template("index.html")

# configuracion de archivo principal de ejecución.
if __name__ == '__main__':
    #configurando el puerto de escucha del servicio web
 app.run(port = 80, debug = True)


