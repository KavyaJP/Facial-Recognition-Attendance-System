# FaceMark – Facial Recognition Attendance System 🧠📸

A full-stack facial recognition-based attendance system built with ReactJS (frontend) and Flask (backend), using OpenCV and face_recognition for face detection and recognition.

## 🔥 Features

- Real-time face recognition using webcam
- Automatic attendance logging for known faces
- On-the-spot registration for unknown faces
- ReactJS frontend for clean, interactive UI
- Flask backend with REST APIs for face recognition and logging
- SQLite/CSV-based attendance database

---

## 🧱 Tech Stack

### Frontend

- ReactJS
- react-webcam
- Axios
- TailwindCSS or Bootstrap (optional)

### Backend

- Python + Flask
- OpenCV
- face_recognition
- SQLite / CSV

---

## 🛠️ Project Structure

```
FaceMark/
├── frontend/         # React app
├── backend/          # Flask app
│   ├── app.py
│   ├── encodings.pkl
│   ├── face_recognition/
│   └── attendance.csv
├── readme.md
├── .gitignore
```

---

## 🚀 Setup Instructions

### Backend (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend (ReactJS)

```bash
cd frontend
npm install
npm run dev  # or npm start
```

---

## 📡 API Overview

### POST /recognize-face

Detects and recognizes face from image.

**Request:** base64 image  
**Response:**

```json
{ "status": "recognized", "id": "123", "name": "John Doe" }
```

Or:

```json
{ "status": "unknown" }
```

---

### POST /register-user

Registers a new face with name and ID.

**Request:**

```json
{ "id": "124", "name": "Jane Doe", "image": "base64string" }
```

**Response:**

```json
{ "success": true }
```

---

### GET /attendance

Fetches today’s attendance log.

---

## 🧠 Future Improvements

- Add liveness detection
- Push notifications for attendance
- Cloud DB and hosting

---

## 🧑‍💻 Author

Kavya Prajapati – [GitHub](https://github.com/KavyaJP)

[kavya31052005@gmail.com](mailto:kavya31052005@gmail.com)
