import './index.css';
import Navbar from "./Features/Common/Navbar/Navbar";
import { BrowserRouter, Route, Routes, useLocation } from "react-router-dom";
import PostPage from './Features/PostPage/PostPage';
import NewsPage from './Features/NewsPage/NewsPage';
import LoginPage from './Features/LoginPage/LoginPage';
import RegisterPage from './Features/RegisterPage/register';
import ProfilePage from './Features/ProfilePage/ProfilePage';
import PrivateRoute from './utils/PrivateRoute';

function App() {
  const location = useLocation();

  return (
    <>
      <main>
      {location.pathname !== '/' && location.pathname !== '/register' && <Navbar />}
        <Routes>
          <Route path='/' element={<LoginPage />} />
          <Route path='/news' element={<NewsPage />} />
          <Route path='/posts' element={<PostPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/profile" element={<ProfilePage />} />
        </Routes>
      </main>
    </>
  );
}

export default App
