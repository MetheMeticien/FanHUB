import React from 'react';
import { FaThumbsUp, FaCommentAlt, FaTrash } from 'react-icons/fa';
import './PostCard.css';

const PostCard = ({
    content, // Renamed from 'text' to 'content' for consistency
    fanName,
    profilePic,
    timestamp,
    imageSrc,
    likes,
    comments,
    liked,
    onLike,
    onDelete,
    onExpand,
    expanded,
    onAddComment,
    mediaType, // New prop to determine media type (image or video)
    mediaUrl,  // New prop to hold the media URL
    isUserPost // New prop to check if this is the user's post
}) => {
    const handleCommentSubmit = (e) => {
        if (e.key === 'Enter' && e.target.value.trim()) {
            onAddComment(e.target.value.trim());
            e.target.value = ''; // Clear input after submitting
        }
    };

    return (
        <div className="post-card">
            {/* Post Header */}
            <div className="post-card-header">
                <img
                    src={profilePic || 'https://via.placeholder.com/50'}
                    alt={`${name}'s profile`}
                    className="profile-pic"
                />
                <div className="post-info">
                    <div className="post-user-name">{fanName || 'Unknown User'}</div>
                    <small className="post-timestamp">
                        {timestamp ? new Date(timestamp).toLocaleString() : 'No Date'}
                    </small>
                </div>
            </div>

            {/* Post Content */}
            <div className="post-card-body">
                <div className="post-description">
                    <p>{content}</p> {/* Displaying the content here */}
                </div>

                {/* Conditionally render the media content (image or video) */}
                {mediaType === 'image' && imageSrc ? (
                    <div className="post-media-wrapper">
                        <img src={imageSrc} alt="Post visual content" className="post-media" />
                    </div>
                ) : mediaType === 'video' && mediaUrl ? (
                    <div className="post-media-wrapper">
                        <video controls className="post-media">
                            <source src={mediaUrl} type="video/mp4" />
                            Your browser does not support the video tag.
                        </video>
                    </div>
                ) : (
                    <p>No media available</p>
                )}
            </div>

            {/* Post Actions */}
            <div className="post-actions">
                <button className={`like-button ${liked ? 'liked' : ''}`} onClick={onLike}>
                    <FaThumbsUp /> {liked ? 'Dislike' : 'Like'} ({likes})
                </button>
                <button className="comment-button" onClick={onExpand}>
                    <FaCommentAlt /> Comment ({comments ? comments.length : 0})
                </button>

                {isUserPost && ( // Only show delete button for user's own posts
                    <button className="delete-button" onClick={onDelete}>
                        <FaTrash /> Delete
                    </button>
                )}
            </div>

            {/* Comments Section */}
            {expanded && (
                <div className="comments-section">
                    <div className="comments">
                        {comments.length > 0 ? (
                            comments.map((comment, index) => (
                                <div key={index} className="comment">
                                    {comment}
                                </div>
                            ))
                        ) : (
                            <div>No comments yet</div>
                        )}
                    </div>

                    {/* Add a comment */}
                    <input
                        type="text"
                        className="comment-input"
                        placeholder="Write a comment..."
                        onKeyDown={handleCommentSubmit}
                    />
                </div>
            )}
        </div>
    );
};

export default PostCard;
