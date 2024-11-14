import React, { useState } from 'react';
import './PostPage.css';
import PostCard from './PostCard';
import { FaClock, FaStar, FaPlus } from 'react-icons/fa';
import Dock from '../Common/Dock/Dock';

const initialPosts = [
    { 
        postId: 'post1', 
        fanName: 'Ruhan', 
        fanPhoto: 'https://via.placeholder.com/50', 
        content: 'Excited about the new rocket launch!', 
        celebrityId: 'elon', 
        timestamp: new Date(),
        likes: 0,
        liked: false,
        comments: [],
        mediaType: 'image',
        mediaUrl: 'https://via.placeholder.com/500'
    },
    { 
        postId: 'post2', 
        fanName: 'Ali', 
        fanPhoto: 'https://via.placeholder.com/50', 
        content: 'Beyoncé is amazing! Can’t wait for the concert!', 
        celebrityId: 'beyonce', 
        timestamp: new Date(),
        likes: 0,
        liked: false,
        comments: [],
        mediaType: 'video',  
        mediaUrl: 'https://www.w3schools.com/html/mov_bbb.mp4' 
    },
    { 
        postId: 'post3', 
        fanName: 'Maya', 
        fanPhoto: 'https://via.placeholder.com/50', 
        content: 'Ronaldo is the best footballer!', 
        celebrityId: 'ronaldo', 
        timestamp: new Date(),
        likes: 0,
        liked: false,
        comments: [],
        mediaType: 'image',
        mediaUrl: 'https://via.placeholder.com/500'
    }
];

const followedCelebrities = [
    { name: 'Elon Musk', id: 'elon' }, 
    { name: 'Beyoncé', id: 'beyonce' }, 
    { name: 'Cristiano Ronaldo', id: 'ronaldo' }
];

function PostPage() {
    const [posts, setPosts] = useState(initialPosts);
    const [selectedCelebrityId, setSelectedCelebrityId] = useState('');  // Track selected celebrity
    const [newPostContent, setNewPostContent] = useState('');
    const [expandedPostIndex, setExpandedPostIndex] = useState(null);
    const [selectedFilter, setSelectedFilter] = useState('newest');

    const handleCreatePost = () => {
        if (newPostContent.trim()) {
            const newPost = {
                postId: `post${posts.length + 1}`, // Incremental post ID
                fanName: 'Ruhan',
                fanPhoto: 'https://via.placeholder.com/50',
                content: newPostContent,
                celebrityId: 'elon', // The post can be about a specific celebrity
                timestamp: new Date(),
                likes: 0,
                liked: false,
                comments: []
            };
            setPosts([newPost, ...posts]);
            setNewPostContent('');
        }
    };

    const handleLikePost = (indexToToggle) => {
        const updatedPosts = posts.map((post, index) => {
            if (index === indexToToggle) {
                return {
                    ...post,
                    likes: post.liked ? post.likes - 1 : post.likes + 1,
                    liked: !post.liked
                };
            }
            return post;
        });
        setPosts(updatedPosts);
    };

    const handleDeletePost = (indexToDelete) => {
        if (window.confirm("Are you sure you want to delete this post?")) {
            const updatedPosts = posts.filter((_, index) => index !== indexToDelete);
            setPosts(updatedPosts);
        }
    };

    const handleFilterNewest = () => {
        const sorted = [...posts].sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
        setPosts(sorted);
        setSelectedFilter('newest');
    };

    const handleFilterPopular = () => {
        const sorted = [...posts].sort((a, b) => b.likes - a.likes);
        setPosts(sorted);
        setSelectedFilter('popular');
    };

    const toggleExpandPost = (index) => {
        setExpandedPostIndex(index === expandedPostIndex ? null : index);
    };

    const handleAddComment = (index, comment) => {
        const updatedPosts = posts.map((post, idx) => {
            if (idx === index) {
                return {
                    ...post,
                    comments: [...post.comments, comment]
                };
            }
            return post;
        });
        setPosts(updatedPosts);
    };

    // Filter posts by selected celebrityId
    const filteredPosts = selectedCelebrityId
        ? posts.filter(post => post.celebrityId === selectedCelebrityId)
        : posts;

    return (
        <div className="post-page-container">
            {/* Left Pane: Celebrities List */}
            <div className="left-pane">
                <h3>Celebrity I Follow</h3>
                <ul className="celebrity-list">
                    {followedCelebrities.map((celebrity) => (
                        <li 
                            key={celebrity.id} 
                            onClick={() => setSelectedCelebrityId(celebrity.id)}
                        >
                            {celebrity.name}
                        </li>
                    ))}
                </ul>
            </div>

            {/* Middle Pane: Post Section */}
            <div className="middle-pane">
                <div className="post-section">
                    {filteredPosts.map((post, index) => (
                        <PostCard
                            key={post.postId}
                            fanName={post.fanName}
                            fanPhoto={post.fanPhoto}
                            content={post.content}
                            timestamp={post.timestamp}
                            imageSrc={post.mediaUrl}
                            mediaType={post.mediaType}
                            likes={post.likes}
                            comments={post.comments}
                            liked={post.liked}
                            onLike={() => handleLikePost(index)}
                            onDelete={() => handleDeletePost(index)}
                            onExpand={() => toggleExpandPost(index)}
                            expanded={expandedPostIndex === index}
                            onAddComment={(comment) => handleAddComment(index, comment)}
                        />
                    ))}
                </div>
            </div>

            {/* Right Pane: Sort By Options */}
            <div className="right-pane">
                <div className="sort-by-title">Sort By:</div>
                <div className="filter-buttons">
                    <button
                        className={`filter-btn ${selectedFilter === 'newest' ? 'selected' : ''}`}
                        onClick={handleFilterNewest}
                    >
                        <FaClock /> Newest
                    </button>
                    <button
                        className={`filter-btn ${selectedFilter === 'popular' ? 'selected' : ''}`}
                        onClick={handleFilterPopular}
                    >
                        <FaStar /> Popular
                    </button>
                </div>
            </div>

            {/* Floating Create Post Button */}
            <button className="create-post-float-btn" onClick={handleCreatePost}>
                <FaPlus />
            </button>

            {/* Floating Dock with buttons */}
            <Dock />
        </div>
    );
}

export default PostPage;
