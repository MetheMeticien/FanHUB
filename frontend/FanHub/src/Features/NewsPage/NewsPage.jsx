// src/NewsGrid.js

import React, { useState, useEffect } from 'react';
import './newspage.css';

const NewsPage = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

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

  if (loading) {
    return <p>Loading news...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="news-grid">
      {news.map((article, index) => (
        <div className="news-card" key={index}>
          <h3>{article.title}</h3>
          <p>{article.content.substring(0, 150)}...</p>
        </div>
      ))}
    </div>
  );
};

export default NewsPage;
