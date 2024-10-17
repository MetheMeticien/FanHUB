import { useState } from 'react';
import './App.css';
import Navbar from "./Features/Common/Navbar/Navbar";
import { BrowserRouter as Router, Route, Routes, useLocation } from "react-router-dom";
import PostPage from './Features/PostPage/PostPage';
import NewsPage from './Features/NewsPage/NewsPage';
import LoginPage from './Features/LoginPage/LoginPage';
import RegisterPage from './Features/RegisterPage/register';

function App() {
  const location = useLocation();

  return (
    <>
      <main>
        //{location.pathname !== '/' && location.pathname !== '/register' && <Navbar />} {/* Render Navbar only if not on LoginPage */}
        <Routes>
          <Route path='/' element={<LoginPage />} />
          <Route path='/news' element={<NewsPage />} />
          <Route path='/posts' element={<PostPage />} />
          <Route path="/register" element={<RegisterPage />} />
        </Routes>
      </main>
    </>
  );
}

export default App
