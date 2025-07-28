import face_recognition
import numpy as np
import cv2
import pickle
import os
from datetime import datetime

ENCODINGS_PATH = "encodings.pkl"
ATTENDANCE_CSV = "attendance.csv"


def load_encodings():
    if os.path.exists(ENCODINGS_PATH):
        with open(ENCODINGS_PATH, "rb") as f:
            return pickle.load(f)
    return {"encodings": [], "names": []}


def save_encodings(data):
    with open(ENCODINGS_PATH, "wb") as f:
        pickle.dump(data, f)


def recognize_face(image_np):
    known_data = load_encodings()
    face_locations = face_recognition.face_locations(image_np)
    face_encodings = face_recognition.face_encodings(image_np, face_locations)

    for encoding in face_encodings:
        matches = face_recognition.compare_faces(known_data["encodings"], encoding)
        if True in matches:
            match_index = matches.index(True)
            name = known_data["names"][match_index]
            mark_attendance(name)
            return {"status": "recognized", "name": name}

    return {"status": "unknown"}


def register_face(name, image_np):
    known_data = load_encodings()
    face_locations = face_recognition.face_locations(image_np)
    face_encodings = face_recognition.face_encodings(image_np, face_locations)

    if face_encodings:
        known_data["encodings"].append(face_encodings[0])
        known_data["names"].append(name)
        save_encodings(known_data)
        return {"success": True}
    else:
        return {"success": False, "error": "No face found"}


def mark_attendance(name):
    now = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
    with open(ATTENDANCE_CSV, "a") as f:
        f.write(f"{name},{now}\n")


def get_today_attendance():
    today = datetime.now().strftime("%Y-%m-%d")
    logs = []

    if os.path.exists(ATTENDANCE_CSV):
        with open(ATTENDANCE_CSV, "r") as f:
            for line in f:
                name, datetime_str = line.strip().split(",")
                date_str, _ = datetime_str.split(" ")
                if today in line:
                    logs.append({"name": name, "timestamp": datetime_str})

    return logs
