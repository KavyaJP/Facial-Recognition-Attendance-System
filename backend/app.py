from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import numpy as np
import cv2
from recognizer_module import recognizer

app = Flask(__name__)
CORS(app)


def base64_to_image(base64_str):
    try:
        img_data = base64.b64decode(base64_str)
        nparr = np.frombuffer(img_data, np.uint8)
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except:
        return None


@app.route("/recognize-face", methods=["POST"])
def recognize():
    data = request.get_json()
    image = base64_to_image(data["image"])
    if image is None:
        return jsonify({"error": "Invalid image data"}), 400
    result = recognizer.recognize_face(image)
    return jsonify(result)


@app.route("/register-user", methods=["POST"])
def register():
    data = request.get_json()
    name = data["name"]
    image = base64_to_image(data["image"])
    if image is None:
        return jsonify({"error": "Invalid image data"}), 400
    result = recognizer.register_face(name, image)
    return jsonify(result)


@app.route("/attendance", methods=["GET"])
def attendance():
    logs = recognizer.get_today_attendance()
    return jsonify(logs)


if __name__ == "__main__":
    app.run(debug=True)
