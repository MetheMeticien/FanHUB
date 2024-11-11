import React, { useState } from 'react';
import './PostPage.css';

const initialCelebrities = [
    // { name: 'Elon Musk', photo: 'https://via.placeholder.com/50', content: 'Launching a new rocket tomorrow!' },
    // { name: 'Beyoncé', photo: 'https://via.placeholder.com/50', content: 'New album out now!' },
    // { name: 'Cristiano Ronaldo', photo: 'https://via.placeholder.com/50', content: 'Scored another hat-trick!' }

        { name: 'Elon Musk', photo: 'https://via.placeholder.com/50', content: 'Launching a new rocket tomorrow!', likes: 0, liked: false },
        { name: 'Beyoncé', photo: 'https://via.placeholder.com/50', content: 'New album out now!', likes: 0, liked: false },
        { name: 'Cristiano Ronaldo', photo: 'https://via.placeholder.com/50', content: 'Scored another hat-trick!', likes: 0, liked: false }

    

    
];

const followedCelebrities = ['Elon Musk', 'Beyoncé', 'Cristiano Ronaldo', 'Selena Gomez', 'Will Smith'];

function PostPage() {
    const [dummyCelebrities, setDummyCelebrities] = useState(initialCelebrities);
    const [newPostContent, setNewPostContent] = useState('');

    // const handleCreatePost = () => {
    //     if (newPostContent.trim()) {
    //         const newPost = {
    //             name: 'Ruhan',
    //             photo: 'https://via.placeholder.com/50',
    //             content: newPostContent
    //         };

    //         setDummyCelebrities([newPost, ...dummyCelebrities]);
    //         setNewPostContent('');
    //     }
    // };


    const handleCreatePost = () => {
        if (newPostContent.trim()) {
            const newPost = {
                name: 'Ruhan',
                photo: 'https://via.placeholder.com/50',
                content: newPostContent,
                timestamp: new Date(),
                likes: 0, 
                liked: false 
            };
    
            setDummyCelebrities([newPost, ...dummyCelebrities]);
            setNewPostContent('');
        }
    };

    const handleLikePost = (indexToToggle) => {
        const updatedCelebrities = dummyCelebrities.map((celebrity, index) => {
            if (index === indexToToggle) {
                return {
                    ...celebrity,
                    likes: celebrity.liked ? celebrity.likes - 1 : celebrity.likes + 1, // Increase or decrease likes
                    liked: !celebrity.liked // Toggle liked status
                };
            }
            return celebrity;
        });
        setDummyCelebrities(updatedCelebrities);
    };
    
    

    const handleDeletePost = (indexToDelete) => {
        // Filter out the post to be deleted based on its index
        // const updatedCelebrities = dummyCelebrities.filter((_, index) => index !== indexToDelete);
        // setDummyCelebrities(updatedCelebrities);

        // adding confirmation
        const handleDeletePost = (indexToDelete) => {
            if (window.confirm("Are you sure you want to delete this post?")) {
                const updatedCelebrities = dummyCelebrities.filter((_, index) => index !== indexToDelete);
                setDummyCelebrities(updatedCelebrities);
            }
        };
        
    };




    const handleFilterNewest = () => {
        const sorted = [...dummyCelebrities].sort(
            (a, b) => new Date(b.timestamp) - new Date(a.timestamp)
        );
        setDummyCelebrities(sorted);
    };
    
    const handleFilterPopular = () => {
        const sorted = [...dummyCelebrities].sort((a, b) => b.likes - a.likes);
        setDummyCelebrities(sorted);
    };
    

    return (
        <div>
            {/* Post creation bar */}
            <div className="postbar-container">
                <input
                    type="text"
                    placeholder="Let’s share what’s going on..."
                    className="post-input"
                    value={newPostContent}
                    onChange={(e) => setNewPostContent(e.target.value)}
                />
                <button className="create-post-btn" onClick={handleCreatePost}>
                    Create Post
                </button>
            </div>

            {/* Filter bar with buttons */}
            <div className="filter-container">
                {/* <button className="filter-btn">Newest</button>
                <button className="filter-btn">Popular</button> */}

                <button className="filter-btn" onClick={handleFilterNewest}>Newest</button>
                <button className="filter-btn" onClick={handleFilterPopular}>Popular</button>

                <button className="filter-btn notification-btn">
                    Following <span className="notification-count">24</span>
                </button>
            </div>

            {/* Main layout for sidebar and posts */}
            <div className="main-layout">
                {/* Left sidebar for celebrities I follow */}
                <div className="celebrity-sidebar">
                    <h3>Celebrity I Follow</h3>
                    <ul className="celebrity-list">
                        {followedCelebrities.map((celebrity, index) => (
                            <li key={index}>{celebrity}</li>
                        ))}
                    </ul>
                </div>

                {/* Right section for posts */}
                <div className="post-section">
                    {dummyCelebrities.map((celebrity, index) => (
                        <div key={index} className="post-container">
                            <div className='post-header-content'>
                                <div className="post-header">
                                    <img src={celebrity.photo} alt={`${celebrity.name}'s profile`} />
                                    <div className="username">{celebrity.name}</div>
                                </div>
                                <div className="post-content">{celebrity.content}</div>
                                

                                {/* displaying time */}
                                <div className="post-footer">
                                     <small>{new Date(celebrity.timestamp).toLocaleString()}</small>
                                </div>

                                {/* handling likes */}
                                <div className="like-container">
                                    <button
                                        className={`like-post-btn ${celebrity.liked ? 'dislike-post-btn' : ''}`}
                                        onClick={() => handleLikePost(index)}
                                    >
                                        {celebrity.liked ? '👎 Dislike' : '👍 Like'} ({celebrity.likes})
                                    </button>
                                </div>




                                
                            </div>
                            <button
                                    className="delete-post-btn"
                                    onClick={() => handleDeletePost(index)}
                                >
                                    Delete Post
                            </button>
                        </div>
                    ))}
                </div>
            </div>
        </div>
        
    );
}

export default PostPage;
