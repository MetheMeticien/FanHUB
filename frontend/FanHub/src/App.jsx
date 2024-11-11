import { useState } from 'react';
import './App.css';
import Navbar from "./Features/Common/Navbar/Navbar";
import { BrowserRouter, Route, Routes, useLocation } from "react-router-dom";
import PostPage from './Features/PostPage/PostPage';
import NewsPage from './Features/NewsPage/NewsPage';
import LoginPage from './Features/LoginPage/LoginPage';
import RegisterPage from './Features/RegisterPage/register';
import PrivateRoute from './utils/PrivateRoute';

function App() {
  const location = useLocation();

  return (
    <>
      <main>
        {location.pathname !== '/' && location.pathname !== '/register' && <Navbar />}

   
          <Routes>
            <Route path="/" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/login" element={<LoginPage />} />


            <Route element={<PrivateRoute />} >
              <Route path="/news" element={<NewsPage />} />
              <Route path="/posts" element={<PostPage />} />

            </Route>
          </Routes>

    
      </main>
    </>
  );
}

export default App
