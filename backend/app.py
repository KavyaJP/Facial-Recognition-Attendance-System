from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "FaceMark Flask Backend Running!"

@app.route('/recognize-face', methods=['POST'])
def recognize_face():
    # TODO: Implement face recognition logic
    return jsonify({"status": "unknown"})

@app.route('/register-user', methods=['POST'])
def register_user():
    # TODO: Save user face encoding
    return jsonify({"success": True})

@app.route('/attendance', methods=['GET'])
def attendance():
    # TODO: Return attendance log
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
