import { useState } from 'react'
import './App.css'
import Navbar from "./Features/Common/Navbar/Navbar"
import { BrowserRouter as Router, Link, Route, Routes } from "react-router-dom";
import HomePage from './Features/HomePage/Homepage';
import PostPage from './Features/PostPage/PostPage';
import NewsPage from './Features/NewsPage/NewsPage';

function App() {

  return (
    <>
        <main >
          <Navbar/>
          <Routes>
            <Route path='/news' element={<NewsPage />} />
            <Route path='/posts' element={<PostPage />} />
            <Route path='/' element={<HomePage />} />
          </Routes>
        </main>
    </>
  )
}

export default App
