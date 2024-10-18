import React, { useState } from 'react';
import './Sidebar.css';

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  const names = ['John Doe', 'Jane Smith', 'Michael Johnson', 'Emily Davis', 'Chris Lee'];

  return (
    <div className={`sidebar ${isOpen ? 'open' : ''}`}>
        <h2>Celebrities</h2>
        <br />
        <br />
        <br />
        
      <button className="toggle-btn" onClick={toggleSidebar}>
        <span className="bar"></span>
        <span className="bar"></span>
        <span className="bar"></span>
      </button>
      <ul className="name-list">
        {isOpen && names.map((name, index) => (
          <li key={index} className="name-item">{name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;
