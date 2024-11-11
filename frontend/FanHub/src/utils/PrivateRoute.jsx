import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import isTokenValid from './isTokenValid';

const PrivateRoute = () => {
  const token = localStorage.getItem('token');
  const isValid = isTokenValid(token);

  // If the token is invalid, redirect to the login page
  return isValid? <Outlet/>: <Navigate to = "/login"/>
};

export default PrivateRoute;
