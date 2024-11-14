import React from 'react';
import { FaThumbsUp, FaCommentAlt, FaTrash } from 'react-icons/fa';
import './PostCard.css';

const PostCard = ({
    imageSrc,
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
    onAddComment
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
                {imageSrc && (
                    <div className="post-image-wrapper">
                        <img src={imageSrc} alt="Post visual content" className="post-image" />
                    </div>
                )}
            </div>

            {/* Post Actions */}
            <div className="post-actions">
                <button className={`like-button ${liked ? 'liked' : ''}`} onClick={onLike}>
                    <FaThumbsUp /> {liked ? 'Dislike' : 'Like'} ({likes})
                </button>
                <button className="comment-button" onClick={onExpand}>
                    <FaCommentAlt /> Comment ({comments.length}) {/* Display the number of comments */}
                </button>
                <button className="delete-button" onClick={onDelete}>
                    <FaTrash /> Delete
                </button>
            </div>

            {/* Expanded Content: Comments */}
            {expanded && (
                <div className="expanded-comments">
                    <h4>Comments</h4>
                    <ul className="comment-list">
                        {comments.map((comment, idx) => (
                            <li key={idx}>{comment}</li> 
                        ))}
                    </ul>
                    <input
                        type="text"
                        placeholder="Add a comment..."
                        className="comment-input"
                        onKeyDown={handleCommentSubmit} // Handle comment submission
                    />
                </div>
            )}
        </div>
    );
};

export default PostCard;
