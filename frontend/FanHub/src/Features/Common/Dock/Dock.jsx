import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaNewspaper, FaUserFriends, FaStar } from 'react-icons/fa';
import './Dock.css';

const Dock = () => {
  const location = useLocation();

  return (
    <div className="dock">
      <Link to="/news">
        <button className={`dock-btn ${location.pathname === '/news' ? 'active' : ''}`}>
          <FaNewspaper />
        </button>
      </Link>
      <Link to="/posts">
        <button className={`dock-btn ${location.pathname === '/posts' ? 'active' : ''}`}>
          <FaUserFriends />
        </button>
      </Link>
      {/* Celebrity page button will be activated later */}
      <Link to="/celebrity">
        <button className={`dock-btn ${location.pathname === '/celebrity' ? 'active' : ''}`}>
          <FaStar />
        </button>
      </Link>
    </div>
  );
};

export default Dock;
