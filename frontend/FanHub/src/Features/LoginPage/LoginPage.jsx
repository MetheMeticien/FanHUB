import React, { useState } from 'react';
import './LoginPage.css';
import { useNavigate } from "react-router-dom";
import logo from '../../assets/logo.png'; // Correct import for the logo
import axios from 'axios';

function LoginPage() {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [token, setToken] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    
    try {
      const response = await axios.post('http://127.0.0.1:8000/token', new URLSearchParams({
        username,
        password
      }), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      });

      localStorage.setItem('token', response.data.access_token);


      navigate('/news');
    } catch (error) {
      setErrorMessage(error.response?.data.detail || 'Login failed');
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
