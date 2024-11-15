import React, { useState, useEffect } from 'react';
import './PostPage.css';
import PostCard from './PostCard';
import { FaClock, FaStar, FaPlus } from 'react-icons/fa';
import Dock from '../Common/Dock/Dock';

const PostPage = ({ celeb_name }) => {
    const [posts, setPosts] = useState([]);
    const [newPostContent, setNewPostContent] = useState('');
    const [expandedPostIndex, setExpandedPostIndex] = useState(null);
    const [selectedFilter, setSelectedFilter] = useState('newest');

    // Fetch posts from API when the component mounts or when celebName prop changes
    useEffect(() => {
        const fetchPosts = async () => {
            try {
                // Use the celeb_name prop to fetch the posts
                const response = await fetch(`http://localhost:8000/posts/for_celeb/${celeb_name}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch posts');
                }
                const data = await response.json();
                console.log(data)
                setPosts(data);
            } catch (error) {
                console.error('Error fetching posts:', error);
            }
        };

        // Fetch posts only if celeb_name exists (avoid fetching empty URL)
        if (celeb_name) {
            fetchPosts();
        }
    }, [celeb_name]); // Re-fetch when celeb_name prop changes

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

    return (
        <div className="post-page-container">
            {/* Left Pane: Celebrities List */}
            <div className="left-pane">
                <h3>Celebrity I Follow</h3>
                <ul className="celebrity-list">
                    {['elon', 'beyonce', 'ronaldo'].map((celebId) => (
                        <li 
                            key={celebId} 
                            onClick={() => setSelectedCelebrityId(celebId)}
                        >
                            {celebId.charAt(0).toUpperCase() + celebId.slice(1)} {/* Capitalize first letter */}
                        </li>
                    ))}
                </ul>
            </div>

            {/* Middle Pane: Post Section */}
            <div className="middle-pane">
                <div className="post-section">
                    {posts.map((post, index) => (
                        <PostCard
                        key={post.postId || index}  // Fallback to index if postId is not reliable
                        fanName={post.fanName}
                        fanPhoto={post.fanPhoto}
                        content={post.content}
                        timestamp={post.timestamp}
                        imageSrc={post.imageUrl}
                        mediaType="image"
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
