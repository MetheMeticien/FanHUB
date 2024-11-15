import React from 'react';
import { BrowserRouter as Router, Routes, Route, Outlet, Link } from 'react-router-dom';

// Function to decode JWT token (without verifying the signature)
const decodeJwt = (token) => {
  try {
    const payload = token.split('.')[1]; // Get the payload part of the JWT
    const decoded = atob(payload); // Decode from Base64
    return JSON.parse(decoded); // Parse the decoded string into a JSON object
  } catch (error) {
    console.error('Error decoding JWT', error);
    return null;
  }
};

// Function to check if the JWT is expired
const isTokenExpired = (decodedToken) => {
  const currentTime = Date.now() / 1000; // Current time in seconds
  return decodedToken.exp && decodedToken.exp < currentTime; // Check if the token is expired
};

// Authentication logic that validates the JWT token
const isAuthenticated = () => {
  const token = localStorage.getItem('token');
  if (token) {
    const decodedToken = decodeJwt(token);
    if (decodedToken && !isTokenExpired(decodedToken)) {
      return true; // Token is valid and not expired
    }
  }
  return false; // Token is missing or expired
};

// Protected Route Component
const ProtectedRoute = ({ children }) => {
  if (!isAuthenticated()) {
    // Redirect to login if not authenticated
    window.location.href = '/login';
    return null;
  }
  return children; // Render the child components if authenticated
};

export default ProtectedRoute;
