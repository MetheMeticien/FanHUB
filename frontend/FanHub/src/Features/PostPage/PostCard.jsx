import React from 'react';
import { FaThumbsUp, FaCommentAlt, FaTrash } from 'react-icons/fa';
import './PostCard.css';

const PostCard = ({
    text,
    name,
    profilePic,
    timestamp,
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
            e.target.value = '';
        }
    };

    return (
        <div className="post-card">
            {/* Post Header */}
            <div className="post-card-header">
                <img src={profilePic} alt={`${name}'s profile`} className="profile-pic" />
                <div className="post-info">
                    <div className="post-user-name">{name || 'Unknown User'}</div>
                    <small className="post-timestamp">
                        {timestamp ? new Date(timestamp).toLocaleString() : 'No Date'}
                    </small>
                </div>
            </div>

            {/* Post Content */}
            <div className="post-card-body">
                <div className="post-description">
                    <p>{text}</p>
                </div>

                {/* Conditionally render the media content (image or video) */}
                {mediaType === 'image' && mediaUrl && (
                    <div className="post-media-wrapper">
                        <img
                            src={mediaUrl}
                            alt="Post visual content"
                            className="post-media"
                        />
                    </div>
                )}
                {mediaType === 'video' && mediaUrl && (
                    <div className="post-media-wrapper">
                        <video
                            controls
                            className="post-media"
                        >
                            <source src={mediaUrl} type="video/mp4" />
                            Your browser does not support the video tag.
                        </video>
                    </div>
                )}
            </div>

            {/* Post Actions */}
            <div className="post-actions">
                <button className={`like-button ${liked ? 'liked' : ''}`} onClick={onLike}>
                    <FaThumbsUp /> {liked ? 'Dislike' : 'Like'} ({likes})
                </button>
                <button className="comment-button" onClick={onExpand}>
                    <FaCommentAlt /> Comment ({comments.length})
                </button>
                {isUserPost && ( // Only show delete button for the logged-in user's posts
                    <button className="delete-button" onClick={onDelete}>
                        <FaTrash /> Delete
                    </button>
                )}
            </div>

            {/* Expanded Content: Comments */}
            {expanded && (
                <div className="expanded-comments">
                    <h4>Comments</h4>
                    <ul className="comment-list">
                        {comments.map((comment, idx) => (
                            <li key={idx}>
                                <strong>{comment.username}</strong>: {comment.text}
                            </li>
                        ))}
                    </ul>
                    <input
                        type="text"
                        className="comment-input"
                        placeholder="Add a comment..."
                        onKeyDown={handleCommentSubmit}
                    />
                </div>
            )}
        </div>
    );
};

export default PostCard;
