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
    // Dummy news data
    const dummyNews = [
      { title: 'Celebrity A hits new record', content: 'Celebrity A has achieved a major milestone in their career...', celebrity: 'Celebrity A' },
      { title: 'Celebrity B announces new project', content: 'Celebrity B is excited to announce their upcoming project...', celebrity: 'Celebrity B' },
      { title: 'Celebrity C wins an award', content: 'Celebrity C has been awarded the Best Actor award for their role in...', celebrity: 'Celebrity C' },
    ];

    // Dummy celebrity data
    const dummyCelebrities = ['Celebrity A', 'Celebrity B', 'Celebrity C'];

    setNews(dummyNews);
    setCelebrities(dummyCelebrities);
    setLoading(false);
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
            All
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
