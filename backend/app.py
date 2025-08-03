from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import numpy as np
import cv2
from recognizer_module import recognizer

app = Flask(__name__)
CORS(app, origins="*", supports_credentials=True)


def base64_to_image(base64_str):
    try:
        image_data = base64.b64decode(base64_str)
        np_arr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        print("[ERROR] in base64_to_image:", str(e))
        return None


import traceback


@app.route("/recognize-face", methods=["POST"])
def recognize_face():
    try:
        data = request.get_json()
        image_data = data["image"]  # base64 string

        image = base64_to_image(image_data)
        if image is None:
            return jsonify({"error": "Invalid image data"}), 400

        result = recognizer.run_face_recognition(image)
        return jsonify({"message": result})

    except Exception as e:
        print("Error in /recognize-face:", e)
        traceback.print_exc()
        return jsonify({"error": "Internal Server Error"}), 500


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
