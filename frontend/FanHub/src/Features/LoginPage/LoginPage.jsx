import React from 'react';
import './LoginPage.css';
import { useNavigate } from "react-router-dom";

function LoginPage() {
  const navigate = useNavigate();

  const handleLogin = () => {
    // Navigate to the home page after login
    navigate('/');
  };

  return (
    <div className="login-page">
      <div className="login-container">
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
