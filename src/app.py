# importamos Flask
from flask import Flask


# paso una instancia de la aplicación
app = flask(__name__)

# Ejecutamos como principal
if __name__ == "__main__":
    app.run(debug=True)
