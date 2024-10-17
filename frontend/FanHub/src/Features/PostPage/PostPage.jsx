import './PostPage.css';

function PostPage() {
    return (
        <div className="post-page">
            {/* Post creation bar */}
            <div className="postbar-container">
                <input type="text" placeholder="Let’s share what’s going on..." className="post-input" />
                <button className="create-post-btn">Create Post</button>
            </div>

            {/* Filter bar with buttons */}
            <div className="filter-container">
                <button className="filter-btn">Newest</button>
                <button className="filter-btn">Popular</button>
                <button className="filter-btn notification-btn">
                    Following <span className="notification-count">24</span>
                </button>
            </div>
        </div>
    );
}

export default PostPage;
