from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada (en memoria)
mensajes = []
contador_id = 1

# GET: Obtener todos los mensajes o uno por ID
@app.route("/mensajes", methods=["GET"])
def obtener_mensajes():
    return jsonify(mensajes), 200


if __name__ == "__main__":
    app.run(debug=True)
