import './index.css';
import Navbar from "./Features/Common/Navbar/Navbar";
import { BrowserRouter, Route, Routes, useLocation } from "react-router-dom";
import PostPage from './Features/PostPage/PostPage';
import LoginPage from './Features/LoginPage/LoginPage';
import RegisterPage from './Features/RegisterPage/register';
import ProfilePage from './Features/ProfilePage/ProfilePage';
import NewsBoard from './Features/News/NewsBoard';
import CelebPage from './Features/Celeb/CelebPage';
import PrivateRoute from './PrivateRoute';
import { useState } from 'react';
import ProtectedRoute from './PrivateRoute';




function App() {
  const location = useLocation();


  return (
    <>
      <main>
      {location.pathname !== '/' && location.pathname !== '/register' && <Navbar />}
        <Routes>
          <Route path='/' element={<LoginPage />} />
          <Route path='/login' element={<LoginPage />} />
          <Route path="/celeb/:celeb_name/*" element={<ProtectedRoute><CelebPage /></ProtectedRoute>} />
          {/* <Route path='/news' element={<NewsBoard />} />
          <Route path='/posts' element={<PostPage />} /> */}
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/profile" element={<ProtectedRoute><ProfilePage /></ProtectedRoute>} />
        </Routes>
      </main>
    </>
  );
}

export default App
