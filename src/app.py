from collections import UserDict
from flask import Flask, json, request, jsonify, Response
from flask_pymongo import PyMongo
# importamos paquetes para trabajar con los passwords
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from werkzeug.wrappers import response
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

    else:
        return not_found()

    return {'message': 'received'}
# listar todos los usuarios (GET)


@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')
# En el caso de datos erroneos

# retornar usuario(GET)


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(user)
    # print(id)
    return Response(response, mimetype="application/json")
# eliminamos usuario(DELETE)


@app.route('/users/<id>', methods=['DELETE'])
def delete_id(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User'+id+'was deleleted successfully'})
    return response

# actualizamos usuario (PUT)


@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if username and email and password:
        hashed_password = generate_password_hash(password)
        mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': {
            'username': username,
            'password': hashed_password,
            'email': email
        }})
        response = jsonify({'message': 'User'+id+'was updated succesfully'})
        return response


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource Not Found: ' + request.url,
        'status': 404

    })
    response.status_code = 404
    return response


# Ejecutamos como principal
if __name__ == "__main__":
    app.run(debug=True)
