# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Daniel" # escribe tu nombre
    age = "16" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
decorator=("/father.jpg")

# define la ruta a la página web de tu madre.
decorator=("/mother.jpeg")


# define la ruta a la página web de tus amigos.
decorator=("/friend.jpg")


# agrega otras rutas, si tú quieres.
decorator=("/me.jpg")




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
