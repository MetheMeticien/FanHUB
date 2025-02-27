import React, { useState } from 'react';
import './PostPage.css';
import PostCard from './PostCard';
import { FaClock, FaStar, FaPlus } from 'react-icons/fa';
import Dock from '../Common/Dock/Dock';
import CreatePost from './CreatePost';  // Import CreatePost component

const initialPosts = [
    { 
        postId: 'post1', 
        fanName: 'Ruhan', 
        fanPhoto: 'https://ecdn.dhakatribune.net/contents/cache/images/800x450x1/uploads/media/2024/07/25/Shafin-Ahmed-Miles-b617ba2cde0019506dd7423c0d3707fc.jpg?jadewits_media_id=24894', 
        content: 'Excited about the new rocket launch!', 
        celebrityId: 'elon', 
        timestamp: new Date(),
        likes: 0,
        liked: false,
        comments: [],
        mediaType: 'image',
        mediaUrl: 'https://dims.apnews.com/dims4/default/49a96f1/2147483647/strip/true/crop/5904x3137+0+0/resize/599x318!/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2F31%2Fa8%2Fe2e760a420e4925e41b6e06cc298%2Fcf21dd697c64497a8c9d26704a88835d'
    },
    { 
        postId: 'post2', 
        fanName: 'Ali', 
        fanPhoto: 'https://via.placeholder.com/50', 
        content: 'Beyoncé is amazing! Can’t wait for the concert!', 
        celebrityId: 'beyonce', 
        timestamp: new Date(),
        likes: 69,
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
        likes: 3,
        liked: false,
        comments: [],
        mediaType: 'image',
        mediaUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTreJaDKN3blcrNMA_5rxXLed4Jo9v1SU3z4w&s'
    }
];

const followedCelebrities = [
    { name: 'Elon Musk', id: 'elon' }, 
    { name: 'Beyoncé', id: 'beyonce' }, 
    { name: 'Cristiano Ronaldo', id: 'ronaldo' }
];

const PostPage = () => {
    const loggedInUser = 'Ruhan';  // Assume "Ruhan" is the logged-in user

    const [posts, setPosts] = useState(initialPosts);
    const [selectedCelebrityId, setSelectedCelebrityId] = useState('');  // Track selected celebrity
    const [newPostContent, setNewPostContent] = useState('');
    const [expandedPostIndex, setExpandedPostIndex] = useState(null);
    const [selectedFilter, setSelectedFilter] = useState('newest');
    const [showCreatePost, setShowCreatePost] = useState(false);  // State for showing the floating CreatePost form

    const handleCreatePost = (newPost) => {
        if (newPost.content.trim()) {
            const postWithMedia = {
                postId: `post${posts.length + 1}`, // Incremental post ID
                fanName: loggedInUser,
                fanPhoto: 'https://via.placeholder.com/50',
                content: newPost.content,
                celebrityId: newPost.celebrityId,
                timestamp: new Date(),
                likes: 0,
                liked: false,
                comments: [],
                mediaType: newPost.mediaType,
                mediaUrl: URL.createObjectURL(newPost.mediaFile),  // Convert media file to URL for display
            };
            setPosts([postWithMedia, ...posts]);
            setShowCreatePost(false);  // Close the CreatePost form after posting
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
                    comments: [...post.comments, { username: loggedInUser, text: comment }]
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

    // Handle selecting a celebrity or "All"
    const handleCelebritySelect = (celebrityId) => {
        if (celebrityId === 'all') {
            setSelectedCelebrityId('');  // Show all posts
        } else {
            setSelectedCelebrityId(celebrityId);
        }
    };

    return (
        <div className="post-page-container">
            {/* Left Pane: Celebrities List with "All" option */}
            <div className="left-pane">
                <h3>Celebrity I Follow</h3>
                <ul className="celebrity-list">
                    <li 
                        onClick={() => handleCelebritySelect('all')}
                        style={{ fontWeight: selectedCelebrityId === '' ? 'bold' : 'normal' }}
                    >
                        All
                    </li>
                    {followedCelebrities.map((celebrity) => (
                        <li 
                            key={celebrity.id} 
                            onClick={() => handleCelebritySelect(celebrity.id)}
                            style={{ fontWeight: selectedCelebrityId === celebrity.id ? 'bold' : 'normal' }}
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
                            onLike={() => handleLikePost(index)}  // Apply actions on all posts
                            onDelete={() => handleDeletePost(index)}  // Apply actions on all posts
                            onExpand={() => toggleExpandPost(index)}  // Apply actions on all posts
                            expanded={expandedPostIndex === index}
                            onAddComment={(comment) => handleAddComment(index, comment)}  // Apply actions on all posts
                            isUserPost={post.fanName === loggedInUser}
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
            <button className="create-post-float-btn" onClick={() => setShowCreatePost(true)}>
                <FaPlus />
            </button>

            {/* Floating CreatePost Form */}
            {showCreatePost && (
                <CreatePost
                    followedCelebrities={followedCelebrities}
                    onCreatePost={handleCreatePost}
                    onClose={() => setShowCreatePost(false)}  // Close the CreatePost form
                />
            )}

            {/* Floating Dock with buttons */}
            <Dock />
            <br />
            <br />
        </div>
    );
};

export default PostPage;
