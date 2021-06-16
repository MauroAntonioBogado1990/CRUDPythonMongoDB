from flask import Flask, request
from flask_pymongo import PyMongo
# importamos paquetes para trabajar con los passwords
from werkzeug.security import generate_password_hash, check_password_hash
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
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if username and email and password:
        # cifrado de contraseña
        hashed_password = generate_password_hash(password)
        # creamos las colecciones
        id = mongo.db.users.insert(
            {'username': username, 'email': email, 'password': hashed_password}
        )
        response = {
            'id': str(id),
            'username': password,
            'password': hashed_password,
            'email': email
        }
        return not_found()
    else:
        {'message': 'received'}

        return {'message': 'received'}


# En el caso de datos erroneos
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    }
    return message


# Ejecutamos como principal
if __name__ == "__main__":
    app.run(debug=True)
