import React from "react";
import './navbar.css';
import { Link } from "react-router-dom";

function Navbar (){
    return(
        <div className="navbar">
            <div className="nav-left">
                <img src="\src\assets\logo.png" alt="Logo" />
            </div>
            <div className="nav-mid">
                <ul>
                    <Link to="/news">
                        <img src="\src\assets\news.png" alt="news-icon" />
                    </Link>
                    <Link to ="/posts">
                        <img src="\src\assets\posts.png" alt="posts-icon" />
                    </Link>
                    <button id="theme-toggle">
                    <img src="\src\assets\ruhan.jpg" alt="Toggle Dark Mode" className="theme-icon" />
                    </button>


                </ul>

            </div>
            <div className="nav-right">
                <img src="\src\assets\ruhan.jpg" alt="profile-pic" />
            </div>

        </div>
    )
}

export default Navbar;