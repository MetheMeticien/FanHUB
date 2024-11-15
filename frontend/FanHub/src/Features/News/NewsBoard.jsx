import { useState, useEffect } from "react";
import axios from "axios";
import NewsItem from "./NewsItem";

const NewsBoard = ({ celeb_name }) => {
  const [articles, setArticles] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        // Update with the actual API endpoint, adjusting for celeb_name if necessary
        const response = await axios.get(`http://localhost:8000/news/by_celeb/Lionel%20Messi`, {
          params: { skip: 0, limit: 100 }
        });
        
        // Map the API response to match NewsItem props structure
        console.log("API Response:", response.data); // Add this line to inspect response data

      // Assuming response.data is an array of news items
      const fetchedArticles = response.data.map(news => ({
        title: news.title,
        description: news.content,
        urlToImage: news.imageUrl,
        url: `https://www.example.com/news/${news.id}`
      }));

      setArticles(fetchedArticles);
    } catch (err) {
      console.error("Error fetching news:", err);
      setError("Failed to load news. Please try again later.");
    }
  };

  fetchNews();
}, [celeb_name]);
  return (
    <div>
      {error && <p>{error}</p>}
      {articles.map((news, index) => (
        <NewsItem
          key={index}
          title={news.title}
          description={news.description}
          src={news.urlToImage}
          url={news.url}
        />
      ))}
    </div>
  );
};

export default NewsBoard;
