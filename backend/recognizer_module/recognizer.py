import face_recognition
import numpy as np
import os
import pickle
import csv
from datetime import datetime, timedelta

ENCODINGS_PATH = "encodings.pkl"
ATTENDANCE_CSV = "attendance.csv"


class Recognizer:
    def __init__(self):
        self.encodings_path = ENCODINGS_PATH
        self.attendance_csv = ATTENDANCE_CSV

    def load_encodings(self):
        if os.path.exists(self.encodings_path):
            with open(self.encodings_path, "rb") as f:
                return pickle.load(f)
        return {"encodings": [], "names": []}

    def save_encodings(self, data):
        with open(self.encodings_path, "wb") as f:
            pickle.dump(data, f)

    def was_recently_logged(self, name, minutes=5):
        if not os.path.exists(self.attendance_csv):
            return False

        now = datetime.now()
        with open(self.attendance_csv, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reversed(list(reader)):
                if len(row) < 2:
                    continue
                last_name, timestamp_str = row
                if last_name == name:
                    try:
                        last_time = datetime.strptime(
                            timestamp_str, "%Y-%m-%d,%H:%M:%S"
                        )
                        if now - last_time < timedelta(minutes=minutes):
                            return True
                    except ValueError:
                        continue
                    break
        return False

    def mark_attendance(self, name):
        if self.was_recently_logged(name):
            return

        now = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
        with open(self.attendance_csv, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, now])

    def recognize_face(self, image_np):
        known_data = self.load_encodings()
        face_locations = face_recognition.face_locations(image_np)
        face_encodings = face_recognition.face_encodings(image_np, face_locations)

        for encoding in face_encodings:
            matches = face_recognition.compare_faces(known_data["encodings"], encoding)
            if True in matches:
                match_index = matches.index(True)
                name = known_data["names"][match_index]
                self.mark_attendance(name)
                return {"status": "recognized", "name": name}

        return {"status": "unknown"}

    def register_face(self, name, image_np):
        known_data = self.load_encodings()
        face_locations = face_recognition.face_locations(image_np)
        face_encodings = face_recognition.face_encodings(image_np, face_locations)

        if face_encodings:
            known_data["encodings"].append(face_encodings[0])
            known_data["names"].append(name)
            self.save_encodings(known_data)
            return {"success": True}
        else:
            return {"success": False, "error": "No face found"}

    def get_today_attendance(self):
        today = datetime.now().strftime("%Y-%m-%d")
        logs = []

        if os.path.exists(self.attendance_csv):
            with open(self.attendance_csv, "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    name, timestamp = row
                    date_str = timestamp.split(",")[0]
                    if date_str == today:
                        logs.append({"name": name, "timestamp": timestamp})

        return logs


recognizer = Recognizer()
