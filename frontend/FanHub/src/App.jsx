import './index.css';
import Navbar from "./Features/Common/Navbar/Navbar";
import { BrowserRouter, Route, Routes, useLocation } from "react-router-dom";
import PostPage from './Features/PostPage/PostPage';
import LoginPage from './Features/LoginPage/LoginPage';
import RegisterPage from './Features/RegisterPage/register';
import ProfilePage from './Features/ProfilePage/ProfilePage';
import NewsBoard from './Features/News/NewsBoard';
import CelebPage from './Features/Celeb/CelebPage';
import { useState } from 'react';




function App() {
  const location = useLocation();


  return (
    <>
      <main>
      {location.pathname !== '/' && location.pathname !== '/register' && <Navbar />}
        <Routes>
          <Route path='/' element={<LoginPage />} />
          <Route path="/celeb/:celeb_name/*" element={<CelebPage />} />
          <Route path='/news' element={<NewsBoard />} />
          <Route path='/posts' element={<PostPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/profile" element={<ProfilePage />} />
        </Routes>
      </main>
    </>
  );
}

export default App
