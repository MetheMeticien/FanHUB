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
        <img src={logo} alt="Logo" className="register-logo" /> {/* Add the logo here */}
        <h1 className="register-title">Register</h1>
        <input type="email" placeholder="Email" className="register-input" />
        <input type="password" placeholder="Password" className="register-input" />
        <input type="password" placeholder="Re-enter Password" className="register-input" />
        <input type="text" placeholder="First Name" className="register-input" />
        <input type="text" placeholder="Last Name" className="register-input" />

        <div className="register-input">
         <input type="radio" name="gender" id="male" value="male" /> 
         <label htmlFor="male">Male</label>

        <input type="radio" name="gender" id="female" value="female" /> 
         <label htmlFor="female">Female</label>
</div>

        <button onClick={handleRegister} className="register-btn">Register</button>

        {/* Temporary button to bypass register for testing */}
        <button onClick={() => navigate('/news')} className="register-btn">Enter Home</button>
      </div>
    </div>
  );
}

export default RegisterPage;
