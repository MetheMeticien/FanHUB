import React, { useState, useEffect } from 'react';
import './ProfilePage.css';

const ProfilePage = () => {
    // Initial profile data (in a real app, this could come from an API or context)
    const [user, setUser] = useState({
        name: 'Ruhan',
        email: 'ahmedshafin@iut-dhaka.edu',
        joined: 'September 1, 2024',
        profilePic: 'https://via.placeholder.com/150' // Placeholder image
    });

    // Editable fields state
    const [editable, setEditable] = useState(false);
    const [name, setName] = useState(user.name);
    const [email, setEmail] = useState(user.email);
    const [profilePic, setProfilePic] = useState(user.profilePic);

    // Toggle edit mode
    const toggleEdit = () => {
        setEditable(!editable);
    };

    // Handle form submit
    const handleSubmit = (e) => {
        e.preventDefault();
        // Update user data
        setUser({ name, email, profilePic, joined: user.joined });
        setEditable(false);
    };

    return (
        <div className="profile-page">
            <div className="profile-header">
                <h1>Your Profile</h1>
                <button onClick={toggleEdit} className="edit-toggle-btn">
                    {editable ? 'Cancel' : 'Edit Profile'}
                </button>
            </div>

            <div className="profile-info">
                <div className="profile-picture">
                    <img
                        src={profilePic}
                        alt="Profile"
                        className="profile-img"
                    />
                </div>
                <div className="profile-details">
                    <form onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="name">Name:</label>
                            <input
                                type="text"
                                id="name"
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                disabled={!editable}
                            />
                        </div>

                        <div className="form-group">
                            <label htmlFor="email">Email:</label>
                            <input
                                type="email"
                                id="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                disabled={!editable}
                            />
                        </div>

                        <div className="form-group">
                            <label htmlFor="profilePic">Profile Picture URL:</label>
                            <input
                                type="text"
                                id="profilePic"
                                value={profilePic}
                                onChange={(e) => setProfilePic(e.target.value)}
                                disabled={!editable}
                            />
                        </div>

                        {editable && (
                            <div className="profile-actions">
                                <button type="submit" className="save-profile-btn">
                                    Save Changes
                                </button>
                            </div>
                        )}
                    </form>
                </div>
            </div>

            <div className="profile-info-footer">
                <p><strong>Joined:</strong> {user.joined}</p>
            </div>
        </div>
    );
};

export default ProfilePage;
