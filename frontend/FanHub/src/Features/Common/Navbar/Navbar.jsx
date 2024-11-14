import React from "react";
import './navbar.css';
import { useNavigate } from "react-router-dom";  // Importing useNavigate for navigation
import { FaSearch } from "react-icons/fa"; // Importing the search icon from react-icons

function Navbar() {
    const navigate = useNavigate(); // Hook for navigation

    // Function to navigate to Profile page
    const handleLogoClick = () => {
        navigate('/profile'); // Redirect to the profile page
    };

    // Function to navigate to News page
    const handleNewsLogoClick = () => {
        navigate('/news'); // Redirect to the news page
    };

    return (
        <div className="navbar">
            <div className="nav-left">
                <img 
                    src="/src/assets/logo.png" 
                    alt="FanHub Logo" 
                    onClick={handleNewsLogoClick} // Add click handler to navigate to the news page
                    style={{ cursor: 'pointer' }} // Make it clear it's clickable
                />
            </div>
            <div className="nav-mid">
                {/* Search Container */}
                <div className="search-container">
                    <input 
                        type="text" 
                        placeholder="Search..." 
                        className="search-bar"
                    />
                    <button className="search-button">
                        <FaSearch /> {/* Using the FaSearch icon here */}
                    </button>
                </div>
            </div>
            <div className="nav-right">
                <img 
                    src="/src/assets/ruhan.jpg" 
                    alt="profile-pic" 
                    onClick={handleLogoClick} // Add click handler to navigate to the profile page
                    style={{ cursor: 'pointer' }} // Make it clear it's clickable
                />
            </div>
        </div>
    );
}

export default Navbar;
