import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ProfilePage.css';
import api from '../Auth/api';

const ProfilePage = () => {
    const [user, setUser] = useState(null); // Store the current user data
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);
  
    useEffect(() => {
        const fetchUserData = async () => {
            try {
              const token = localStorage.getItem("token");
              const response = await api.get(`/me?token=${token}`);  // Pass token in the query string
              setUser(response.data);
              console.log(user);
              setLoading(false);
            } catch (err) {
              console.error("Error fetching user data:", err.response ? err.response.data : err);
              setError('Error fetching user data');
              setLoading(false);
            }
          };
          
    
        fetchUserData();
      }, []);
    
      if (loading) return <h2>Loading...</h2>;
      if (error) return <h2>{error}</h2>;



    return (
        <div className="profile-page">
            <div className="profile-header">
                <h1>Your Profile</h1>
            </div>

            <div className="profile-info">
                <div className="profile-picture">
                    <img
                        src={user.profilePic || 'https://via.placeholder.com/150'} // Assuming profilePic is part of user data
                        alt="Profile"
                        className="profile-img"
                    />
                </div>
                <div className="profile-details">
                    <p><strong>Username:</strong> {user.username}</p>
                    <p><strong>First Name:</strong> {user.firstname}</p>
                    <p><strong>Last Name:</strong> {user.lastname}</p>
                    <p><strong>Gender:</strong> {user.gender}</p>
                    {/* <p><strong>Email:</strong> {user.username}</p> */}
                    {/* <p><strong>Joined:</strong> {user.joined}</p> */}
                </div>
            </div>
        </div>
    );
};

export default ProfilePage;
