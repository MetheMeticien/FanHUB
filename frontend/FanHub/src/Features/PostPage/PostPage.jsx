import React, { useState } from 'react';
import './PostPage.css';
import PostCard from './PostCard';
import { FaClock, FaStar, FaPlus } from 'react-icons/fa';

const initialCelebrities = [
    { name: 'Elon Musk', photo: 'https://via.placeholder.com/50', content: 'Launching a new rocket tomorrow!', likes: 0, liked: false, comments: [] },
    { name: 'Beyoncé', photo: 'https://via.placeholder.com/50', content: 'New album out now!', likes: 0, liked: false, comments: [] },
    { name: 'Cristiano Ronaldo', photo: 'https://via.placeholder.com/50', content: 'Scored another hat-trick!', likes: 0, liked: false, comments: [] }
];

const followedCelebrities = ['Elon Musk', 'Beyoncé', 'Cristiano Ronaldo', 'Selena Gomez', 'Will Smith'];

function PostPage() {
    const [dummyCelebrities, setDummyCelebrities] = useState(initialCelebrities);
    const [newPostContent, setNewPostContent] = useState('');
    const [expandedPostIndex, setExpandedPostIndex] = useState(null);
    const [showCreatePostCard, setShowCreatePostCard] = useState(false);

    const handleCreatePost = () => {
        if (newPostContent.trim()) {
            const newPost = {
                name: 'Ruhan',
                photo: 'https://via.placeholder.com/50',
                content: newPostContent,
                timestamp: new Date(),
                likes: 0, 
                liked: false,
                comments: []
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
                    likes: celebrity.liked ? celebrity.likes - 1 : celebrity.likes + 1,
                    liked: !celebrity.liked
                };
            }
            return celebrity;
        });
        setDummyCelebrities(updatedCelebrities);
    };

    const handleDeletePost = (indexToDelete) => {
        if (window.confirm("Are you sure you want to delete this post?")) {
            const updatedCelebrities = dummyCelebrities.filter((_, index) => index !== indexToDelete);
            setDummyCelebrities(updatedCelebrities);
        }
    };

    const handleFilterNewest = () => {
        const sorted = [...dummyCelebrities].sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
        setDummyCelebrities(sorted);
    };
    
    const handleFilterPopular = () => {
        const sorted = [...dummyCelebrities].sort((a, b) => b.likes - a.likes);
        setDummyCelebrities(sorted);
    };

    const toggleExpandPost = (index) => {
        setExpandedPostIndex(index === expandedPostIndex ? null : index);
    };

    const handleAddComment = (index, comment) => {
        const updatedCelebrities = dummyCelebrities.map((celebrity, idx) => {
            if (idx === index) {
                return {
                    ...celebrity,
                    comments: [...celebrity.comments, comment]
                };
            }
            return celebrity;
        });
        setDummyCelebrities(updatedCelebrities);
    };

    // Function to trigger the file input click
    const triggerFileInput = () => {
        document.getElementById('image-input').click();
    };

    return (
        <div className="post-page-container">
            {/* Left Pane: Celebrities List */}
            <div className="left-pane">
                <h3>Celebrity I Follow</h3>
                <ul className="celebrity-list">
                    {followedCelebrities.map((celebrity, index) => (
                        <li key={index}>{celebrity}</li>
                    ))}
                </ul>
            </div>

            {/* Right Pane: Post Section */}
            <div className="right-pane">
                {/* Floating Create Post Button */}
                <button className="create-post-float-btn" onClick={() => NULL}>
                    <FaPlus />
                </button>

                {/* Filter buttons moved above the posts */}
                <div className="postbar-container">
                    <div className="filter-buttons">
                        <button className="filter-btn" onClick={handleFilterNewest}>
                            <FaClock /> Newest
                        </button>
                        <button className="filter-btn" onClick={handleFilterPopular}>
                            <FaStar /> Popular
                        </button>
                    </div>
                </div>

                <div className="post-section">
                    {dummyCelebrities.map((celebrity, index) => (
                        <PostCard
                            key={index}
                            name={celebrity.name}
                            timestamp={celebrity.timestamp}
                            imageSrc={celebrity.photo}
                            text={celebrity.content}
                            likes={celebrity.likes}
                            comments={celebrity.comments}
                            shares={0} 
                            liked={celebrity.liked}
                            onLike={() => handleLikePost(index)}
                            onDelete={() => handleDeletePost(index)}
                            onExpand={() => toggleExpandPost(index)}
                            expanded={expandedPostIndex === index}
                            onAddComment={(comment) => handleAddComment(index, comment)}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
}

export default PostPage;
