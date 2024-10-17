import React from 'react';
import './register.css';
import { useNavigate } from "react-router-dom";
import logo from '../../assets/logo.png'; 

function RegisterPage() {
  const navigate = useNavigate();

  const handleRegister = () => {
    // Navigate to the home page after register
    navigate('/');
  };

  return (
    <div className="register-page">
      <div className="register-container">
        <div className="register-left">
          <img src={logo} alt="Logo" className="register-logo" />
        </div>
        <div className="register-right">
          <h1 className="register-title">Register</h1>
          <div className="register-inputs">
            <input type="text" placeholder="First Name" className="register-input" />
            <input type="text" placeholder="Last Name" className="register-input" />
            <input type="email" placeholder="Email" className="register-input email-input" />
            <input type="password" placeholder="Password" className="register-input" />
            <input type="password" placeholder="Re-enter Password" className="register-input" />
          </div>

          {/* Gender dropdown */}
          <div className="register-gender-dropdown">
            <select className="register-input" defaultValue="">
              <option value="" disabled>Select Gender</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>

          <button onClick={handleRegister} className="register-btn">Register</button>

          {/* Temporary button to bypass register for testing */}
          <button onClick={() => navigate('/news')} className="register-btn">Enter Home</button>
        </div>
      </div>
    </div>
  );
}

export default RegisterPage;
