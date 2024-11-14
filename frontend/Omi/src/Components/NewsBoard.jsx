import { useState, useEffect } from "react";
import NewsItem from "./NewsItem";

const NewsBoard = ({ category }) => {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    // Dummy data for testing
    const dummyData = [
      {
        title: "Breaking News: Something Happened",
        description: "Details about the incident that occurred earlier today.",
        urlToImage: "src/assets/apple.jpeg",
        url: "https://www.example.com/news/1"
      },
      {
        title: "Tech Update: New Gadgets Released",
        description: "A summary of the latest tech gadgets announced this week.",
        urlToImage: "src/assets/Oranges.jpg",
        url: "https://www.example.com/news/2"
      },
      {
        title: "Sports: Championship Results",
        description: "The results from the latest championship game.",
        urlToImage: "src/assets/ruhan.jpg",
        url: "https://www.example.com/news/3"
      }
    ];

    setArticles(dummyData);
  }, [category]);

  return (
    <div>
      {/* <h2 className="text-center">
        Latest <span className="badge bg-danger">News</span>
      </h2> */}
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
