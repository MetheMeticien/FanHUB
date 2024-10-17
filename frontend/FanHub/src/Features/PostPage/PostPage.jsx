import './PostPage.css';

const dummyCelebrities = [
    { name: 'Elon Musk', photo: 'https://via.placeholder.com/50', content: 'Launching a new rocket tomorrow!' },
    { name: 'Beyoncé', photo: 'https://via.placeholder.com/50', content: 'New album out now!' },
    { name: 'Cristiano Ronaldo', photo: 'https://via.placeholder.com/50', content: 'Scored another hat-trick!' }
];

const followedCelebrities = ['Elon Musk', 'Beyoncé', 'Cristiano Ronaldo', 'Selena Gomez', 'Will Smith'];

function PostPage() {
    return (
        <div>
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
                            <div className="post-header">
                                <img src={celebrity.photo} alt={`${celebrity.name}'s profile`} />
                                <div className="username">{celebrity.name}</div>
                            </div>
                            <div className="post-content">{celebrity.content}</div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default PostPage;
