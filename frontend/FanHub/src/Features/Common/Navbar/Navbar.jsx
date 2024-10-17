import React from "react";
import './navbar.css';
import { Link, useLocation } from "react-router-dom";

function Navbar() {
    const location = useLocation(); // Get current route

    return (
        <div className="navbar">
            <div className="nav-left">
                <img src="/src/assets/logo.png" alt="Logo" />
            </div>
            <div className="nav-mid">
                <ul>
                    <li className={location.pathname === '/news' ? 'active' : ''}>
                        <Link to="/news">
                            <img src="/src/assets/news.png" alt="news-icon" />
                        </Link>
                    </li>
                    <li className={location.pathname === '/posts' ? 'active' : ''}>
                        <Link to="/posts">
                            <img src="/src/assets/posts.png" alt="posts-icon" />
                        </Link>
                    </li>
                </ul>
            </div>
            <div className="nav-right">
                <img src="/src/assets/ruhan.jpg" alt="profile-pic" />
            </div>
        </div>
    );
}

export default Navbar;
