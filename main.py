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

# PUT: Actualizar un mensaje existente
@app.route("/mensajes/<int:mensaje_id>", methods=["PUT"])
def actualizar_mensaje(mensaje_id):
    data = request.get_json()
    for mensaje in mensajes:
        if mensaje["id"] == mensaje_id:
            mensaje["user"] = data.get("user", mensaje["user"])
            mensaje["mensaje"] = data.get("mensaje", mensaje["mensaje"])
            return jsonify(mensaje), 200
    return jsonify({"error": "Mensaje no encontrado"}), 404

# DELETE: Eliminar un mensaje
@app.route("/mensajes/<int:mensaje_id>", methods=["DELETE"])
def eliminar_mensaje(mensaje_id):
    for mensaje in mensajes:
        if mensaje["id"] == mensaje_id:
            mensajes.remove(mensaje)
            return jsonify({"mensaje": "Mensaje eliminado"}), 200
    return jsonify({"error": "Mensaje no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
