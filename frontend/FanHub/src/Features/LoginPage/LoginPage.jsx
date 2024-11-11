import React, { useState } from 'react';
import './LoginPage.css';
import { useNavigate } from "react-router-dom";
import logo from '../../assets/logo.png'; // Correct import for the logo

function LoginPage() {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    // console.log("HI")
    try {
      const response = await api.post("/token", new URLSearchParams({
        username,
        password
      }));
      console.log(response)
      const { access_token } = response.data;
      localStorage.setItem("access_token", access_token); // Store token in localStorage
      navigate("/posts"); // Redirect to protected route
    } catch (err) {
      setError("Incorrect username or password");
    }
  };

  const handleRegister = () => {
    navigate('/register');
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <div className="login-left">
          <img src={logo} alt="Logo" className="login-logo" />
        </div>
        <div className="login-right">
          <h1 className="login-title">Welcome</h1>
          <input
            className='login-input'
            type="text"
            value={username}
            placeholder='Username'
            onChange={(e) => setUsername(e.target.value)}
          />
           <input
            className='login-input'
            type="password"
            value={password}
            placeholder='Password'
            onChange={(e) => setPassword(e.target.value)}
          />
          <button onClick={handleLogin} className="login-btn">Login</button>
          <button onClick={handleRegister} className="register-btn">Register</button>

          {/* Temporary button to bypass login for testing */}
          {/* <button onClick={() => navigate('/news')} className="login-btn">Enter Home</button> */}
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
