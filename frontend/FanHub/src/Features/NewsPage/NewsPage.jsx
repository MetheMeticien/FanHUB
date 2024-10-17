import React, { useState, useEffect } from 'react';
import './newspage.css';

const NewsPage = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filter, setFilter] = useState('All Following');
  const [viewMode, setViewMode] = useState('grid'); // 'grid' or 'list'
  const [celebrities, setCelebrities] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/news');
        if (!response.ok) {
          throw new Error('Failed to fetch news');
        }
        const data = await response.json();
        setNews(data);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };

    const fetchCelebrities = async () => {
      // Assuming your backend provides a list of celebrities
      const response = await fetch('http://127.0.0.1:5000/api/celebrities');
      const data = await response.json();
      setCelebrities(data);
    };

    fetchNews();
    fetchCelebrities();
  }, []);

  const handleFilterChange = (celebrity) => {
    setFilter(celebrity);
  };

  const toggleViewMode = () => {
    setViewMode(viewMode === 'grid' ? 'list' : 'grid');
  };

  const getFilteredNews = () => {
    if (filter === 'All Following') {
      return news; // Return all news from followed celebrities
    } else {
      return news.filter((article) => article.celebrity === filter); // Filter news by selected celebrity
    }
  };

  if (loading) {
    return <p>Loading news...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="news-page-container">
      {/* Left Pane: List of Celebrities */}
      <div className="left-pane">
        <h3>Following</h3>
        <ul>
          <li 
            className={filter === 'All Following' ? 'active' : ''} 
            onClick={() => handleFilterChange('All Following')}
          >
            All Following
          </li>
          {celebrities.map((celebrity) => (
            <li
              key={celebrity}
              className={filter === celebrity ? 'active' : ''}
              onClick={() => handleFilterChange(celebrity)}
            >
              {celebrity}
            </li>
          ))}
        </ul>
      </div>

      {/* Right Pane: News Articles */}
      <div className="right-pane">
        {/* Toggle between Grid and List View */}
        <button onClick={toggleViewMode}>
          Switch to {viewMode === 'grid' ? 'List' : 'Grid'} View
        </button>

        {/* News Grid/List */}
        <div className={`news-grid ${viewMode}-view`}>
          {getFilteredNews().map((article, index) => (
            <div className="news-card" key={index}>
              <h3>{article.title}</h3>
              <p>{article.content.substring(0, 150)}...</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default NewsPage;
