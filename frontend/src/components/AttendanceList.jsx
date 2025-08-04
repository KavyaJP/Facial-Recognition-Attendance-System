import React, { useEffect, useState } from "react";
import axios from "axios";

const AttendanceList = () => {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:5000/attendance")
      .then((res) => {
        if (res.data && Array.isArray(res.data.attendance)) {
          setEntries(res.data.attendance);
        } else {
          setEntries([]); // fallback in case format is wrong
        }
      })
      .catch((err) => {
        console.error("Error fetching attendance:", err);
        setEntries([]);
      });
  }, []);

  return (
    <div className="mt-6">
      <h2 className="text-xl font-semibold mb-2">Attendance List</h2>
      {entries.length > 0 ? (
        <ul className="list-disc pl-6">
          {entries.map((entry, idx) => (
            <li key={idx}>{entry}</li>
          ))}
        </ul>
      ) : (
        <p className="text-gray-500">No attendance records yet.</p>
      )}
    </div>
  );
};

export default AttendanceList;
