from flask import Flask
from flask_pymongo import PyMongo
# paso una instancia de la aplicación
app = Flask(__name__)
# propiedades de la DB
app.config['MONGO_URI'] = 'mongodb://localhost/pythonMongoDB'

# realizamos la conección
mongo = PyMongo(app)
# creamos la ruta- Crear usuarios


@app.route('/users', methods=['POST'])
def create_user():
    # Recibiendo datos
    return {'message': 'received'}


# Ejecutamos como principal
if __name__ == "__main__":
    app.run(debug=True)
