import './index.css';
import Navbar from "./Features/Common/Navbar/Navbar";
import { BrowserRouter, Route, Routes, useLocation } from "react-router-dom";
import PostPage from './Features/PostPage/PostPage';
import LoginPage from './Features/LoginPage/LoginPage';
import RegisterPage from './Features/RegisterPage/register';
import NewsBoard from './Features/News/NewsBoard';
import { useState } from 'react';




function App() {
  const location = useLocation();

  const [category, setCategory] = useState("entertainment");

  return (
    // <ChakraProvider>  {/* Wrap your app with ChakraProvider */}
    <main>
      {/* {location.pathname !== '/' && location.pathname !== '/register' && <Navbar />} */}
      <Routes>
        <Route path='/' element={<LoginPage />} />
        <Route path="/celeb/:celeb_name/news" element={<NewsBoard category={category}/>}/>
        <Route path='/news' element={<NewsBoard category={category} />} />
        <Route path='/posts' element={<PostPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </main>
    // </ChakraProvider>
  );
}

export default App
