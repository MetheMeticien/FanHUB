import './PostPage.css';
function PostPage() {
    return (
        <div className="post-page">
            <div className="postbar-container">
                <input type="text" placeholder="Let’s share what’s going..." className="post-input" />
                <button className="create-post-btn">Create Post</button>
            </div>

            <div className="filter-container">
                <button className="filter-btn">
                    <img src="/src/assets/newest-icon.png" alt="Newest" className="filter-icon" />
                    Newest
                </button>
                <button className="filter-btn">
                    <img src="/src/assets/popular-icon.png" alt="Popular" className="filter-icon" />
                    Popular
                </button>
                <button className="filter-btn notification-btn">
                    <img src="/src/assets/following-icon.png" alt="Following" className="filter-icon" />
                    Following <span className="notification-count">24</span>
                </button>
            </div>
        </div>
    );
}

export default PostPage;
