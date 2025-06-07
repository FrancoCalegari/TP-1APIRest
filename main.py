from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada (en memoria)
mensajes = []
contador_id = 1

# GET: Obtener todos los mensajes o uno por ID
@app.route("/mensajes", methods=["GET"])
def obtener_mensajes():
    return jsonify(mensajes), 200
@app.route("/mensajes/<int:mensaje_id>", methods=["GET"])
def obtener_mensaje(mensaje_id):
    for mensaje in mensajes:
        if mensaje["id"] == mensaje_id:
            return jsonify(mensaje), 200
    return jsonify({"error": "Mensaje no encontrado"}), 404

# POST: Crear un nuevo mensaje
@app.route("/mensajes", methods=["POST"])
def crear_mensaje():
    global contador_id
    data = request.get_json()
    nuevo_mensaje = {
        "id": contador_id,
        "user": data.get("user"),
        "mensaje": data.get("mensaje")
    }
    mensajes.append(nuevo_mensaje)
    contador_id += 1
    return jsonify(nuevo_mensaje), 201

if __name__ == "__main__":
    app.run(debug=True)
