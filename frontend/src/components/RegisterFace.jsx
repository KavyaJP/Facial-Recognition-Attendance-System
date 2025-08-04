import React, { useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";

const RegisterFace = () => {
  const webcamRef = useRef(null);
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");

  const handleRegister = async () => {
    const screenshot = webcamRef.current.getScreenshot();
    if (!screenshot || !name.trim()) {
      setMessage("Please enter a valid name and capture image.");
      return;
    }

    const base64Image = screenshot.replace(/^data:image\/\w+;base64,/, "");

    try {
      const res = await axios.post("http://localhost:5000/register-user", {
        name,
        image: base64Image,
      });

      if (res.data.success) {
        setMessage("✅ Face registered successfully!");
      } else {
        setMessage("⚠️ Face not recognized in image. Try again.");
      }
    } catch (err) {
      console.error(err);
      setMessage("❌ Registration failed. Check server logs.");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Register New Face</h2>

      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ marginBottom: "10px", padding: "5px" }}
      />

      <div style={{ marginBottom: "10px" }}>
        <Webcam
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={320}
          height={240}
        />
      </div>

      <button onClick={handleRegister} style={{ padding: "8px 12px" }}>
        Register
      </button>

      <p>{message}</p>
    </div>
  );
};

export default RegisterFace;
