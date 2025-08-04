import {
  BrowserRouter as Router,
  Routes,
  Route,
  NavLink,
} from "react-router-dom";
import WebcamCapture from "./components/WebcamCapture";
import RegisterFace from "./components/RegisterFace";
import AttendanceList from "./components/AttendanceList";

function App() {
  return (
    <Router>
      <div className="app-wrapper">
        <h1 className="main-heading">Face Recognition Attendance System</h1>
        <nav className="navbar">
          <NavLink to="/" className="nav-link">
            Recognize Face
          </NavLink>
          <NavLink to="/register" className="nav-link">
            Register Face
          </NavLink>
          <NavLink to="/attendance" className="nav-link">
            Attendance List
          </NavLink>
        </nav>

        <Routes>
          <Route path="/" element={<WebcamCapture />} />
          <Route path="/register" element={<RegisterFace />} />
          <Route path="/attendance" element={<AttendanceList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
