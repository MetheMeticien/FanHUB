import React, { useState, useEffect } from 'react';
import './newspage.css';

const NewsPage = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filter, setFilter] = useState('Newest');

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

    fetchNews();
  }, []);

  const handleFilterChange = (selectedFilter) => {
   setFilter(selectedFilter);
  };

  //Assuming your backend provides sorting or you can sort news locally
  const getFilteredNews = () => {
    switch (filter) {
      case 'Newest':
        return news.sort((a, b) => new Date(b.date) - new Date(a.date)); // Sorting by date, newest first
      case 'Popular':
        return news.sort((a, b) => b.likes - a.likes); // Sorting by popularity, using 'likes'
      case 'Following':
        return news.filter(article => article.following === true); // Showing followed news
      default:
        return news;
    }
  };

  if (loading) {
    return <p>Loading news...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      {/* Filter Container */}
      <div className="filter-container">
        <button 
          className={filter === 'Newest' ? 'filter-button active' : 'filter-button'}
          onClick={() => handleFilterChange('Newest')}
        >
          Newest
        </button>
        <button 
          className={filter === 'Popular' ? 'filter-button active' : 'filter-button'}
          onClick={() => handleFilterChange('Popular')}
        >
          Popular
        </button>
        <button 
          className={filter === 'Following' ? 'filter-button active' : 'filter-button'}
          onClick={() => handleFilterChange('Following')}
        >
          Following
        </button>
      </div>

      {/* News Grid */}
      <div className="news-grid">
        {getFilteredNews().map((article, index) => (
          <div className="news-card" key={index}>
            <h3>{article.title}</h3>
            <p>{article.content.substring(0, 150)}...</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default NewsPage;
