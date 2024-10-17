import React from 'react';
import './LoginPage.css';
import { useNavigate } from "react-router-dom";
import logo from '../../assets/logo.png'; // Correct import for the logo

function LoginPage() {
  const navigate = useNavigate();

  const handleLogin = () => {
    // Navigate to the home page after login
    navigate('/');
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <img src={logo} alt="Logo" className="login-logo" /> {/* Add the logo here */}
        <h1 className="login-title">Welcome</h1>
        <input type="text" placeholder="Username" className="login-input" />
        <input type="password" placeholder="Password" className="login-input" />
        <button onClick={handleLogin} className="login-btn">Login</button>

        {/* Temporary button to bypass login for testing */}
        <button onClick={() => navigate('/news')} className="login-btn">Enter Home</button>
      </div>
    </div>
  );
}

export default LoginPage;
