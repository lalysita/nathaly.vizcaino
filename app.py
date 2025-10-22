# app.py
from flask import Flask

app = Flask(__name__)

# Función para prueba unitaria
def sumar(a, b):
    return a + b

@app.route('/')
def hola_mundo():
    return 'Adiós, Mundo!', 200 # Este cambio hará que la prueba falle

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)