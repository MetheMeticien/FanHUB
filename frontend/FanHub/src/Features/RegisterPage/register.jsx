import React, { useState } from 'react';
import './register.css';
import { useNavigate } from "react-router-dom";
import logo from '../../assets/logo.png';
import axios from "axios"

const RegisterPage = () => {
  const navigate = useNavigate();

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('');
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('');
  const [gender, setGender] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      setMessage("Passwords do not match");
      return;
    }

    try {
      console.log(username)
      console.log(password)
      const response = await axios.post(
        'http://127.0.0.1:8000/register', 
        {
          username: username,
          password: password,
          firstname:firstName,
          lastname: lastName,
          gender:gender
        },
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
      setMessage(`${response.data.username} created successfully! `);
      setUsername('');
      setPassword('');
      setFirstName('');
      setLastName('');
      setConfirmPassword('');
      setGender('');
      navigate('/')
    } catch (error) {
      setMessage(error.response?.data.detail || 'Registration failed');
    }
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
          <input
              type="text"
              placeholder="First Name"
              value={firstName}
              className='register-input'
              onChange={(e) => setFirstName(e.target.value)}
              required
            />
            <input
              type="text"
              placeholder="Last Name"
              value={lastName}
              className='register-input'
              onChange={(e) => setLastName(e.target.value)}
              required
            />
            <input
              type="text"
              placeholder="Username"
              value={username}
              className='register-input'
              onChange={(e) => setUsername(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder="Password"
              value={password}
              className='register-input'
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder="Confirm Password"
              value={confirmPassword}
              className='register-input'
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </div>

          {/* Gender dropdown */}
          <div className="register-gender-dropdown">
            <select onChange={(e) => setGender(e.target.value)} className="register-input" defaultValue="">
              <option value="" disabled>Select Gender</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>

          <button onClick={handleRegister} className="register-btn">Register</button>

          {/* Temporary button to bypass register for testing */}
          <button onClick={() => navigate('/news')} className="register-btn">Enter Home</button>

          <div className='message'>
            <p>{message}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default RegisterPage;
