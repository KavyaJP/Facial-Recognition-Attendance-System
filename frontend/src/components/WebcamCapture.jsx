// frontend/src/components/WebcamCapture.jsx
import React, { useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";

const WebcamCapture = () => {
  const webcamRef = useRef(null);
  const [responseMsg, setResponseMsg] = useState("");

  const capture = async () => {
    const screenshot = webcamRef.current.getScreenshot();

    if (!screenshot) return;

    const base64Data = screenshot.replace(/^data:image\/\w+;base64,/, "");

    try {
      const res = await axios.post(
        "http://localhost:5000/recognize-face",
        { image: base64Data },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const { name, status } = res.data.message || {};
      setResponseMsg(`Status: ${status}, Name: ${name || "Unknown"}`);
    } catch (err) {
      console.error(err);
      setResponseMsg("Error recognizing face");
    }
  };

  return (
    <div className="flex flex-col items-center gap-4">
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={320}
        height={240}
      />
      <button
        onClick={capture}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Capture & Recognize
      </button>
      <p>{responseMsg}</p>
    </div>
  );
};

export default WebcamCapture;
