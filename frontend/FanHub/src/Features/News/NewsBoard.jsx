import { useState, useEffect } from "react";
import axios from "axios";
import NewsItem from "./NewsItem";
import Dock from "../Common/Dock/Dock";
import './news.css';


// Dummy Data for Testing
const dummyData = [
  {
    title: "Apple, MLS and the huge impact of Messi",
    content: "The start of the round of 16 of North America's top soccer league, Major League Soccer...",
    author: "Marca",
    category: "Sports",
    imageUrl: "https://phantom-marca.unidadeditorial.es/aa552715f5fabbfbbd85993f94b06615/resize/828/f/webp/assets/multimedia/imagenes/2024/11/01/17304733709244.jpg",
    id: 1,
  },
  {
    title: "Leo Messi's message after Inter Miami's painful elimination against Atlanta",
    content: "Inter Miami's season ended much earlier than they themselves were expecting...",
    author: "Marca",
    category: "Sports",
    imageUrl: "https://phantom-marca.unidadeditorial.es/baba42b87e7c7476c34227fe4d8ae622/resize/828/f/webp/assets/multimedia/imagenes/2024/11/12/17314333443195.jpg",
    id: 2,
  },
  {
    title: "Leo Messi rules out being a coach... but is unsure about his future",
    content: "In an interview with Fabrizio Romano for '433', Leo Messi spoke about his future, the 2026 World Cup...",
    author: "Marca",
    category: "Sports",
    imageUrl: "https://phantom-marca.unidadeditorial.es/b77ba1ccbc488ed90bacfae0b1fb637d/resize/828/f/webp/assets/multimedia/imagenes/2024/10/31/17304059339766.jpg",
    id: 3,
  },
  {
    title: "LeBron James to be joined by Lionel Messi and Angel Reese in sensational collaboration",
    content: "Los Angeles Lakers star LeBron James, Inter Miami's Lionel Messi and Chicago Sky's Angel Reese are set for a sensational collaboration...",
    author: "Marca",
    category: "Sports",
    imageUrl: "https://phantom-marca.unidadeditorial.es/081fc8321f89c340aeed3c6e9c4520b9/crop/0x0/2044x1363/resize/828/f/webp/assets/multimedia/imagenes/2024/10/30/17303188387568.jpg",
    id: 4,
  },
  {
    title: "No Messi, No Ronaldo. The dawn of a new era in soccer: A new generation of soccer stars is lining up to win the Ballon d'Or",
    content: "When the Ballon d'Or is presented at a gala ceremony in Paris on Monday, it will feel like the start of a new era in soccer...",
    author: "Marca",
    category: "Sports",
    imageUrl: "https://phantom-marca.unidadeditorial.es/c3ceb88a92433afa5d6ad2dc5fda7b73/resize/828/f/webp/assets/multimedia/imagenes/2024/10/27/17300491951902.jpg",
    id: 5,
  },
  {
    title: "Infantino announces that Inter Miami will play in the Club World Cup... after another remarkable performance by Messi",
    content: "Gianni Infantino confirmed at Chase Stadium that Inter Miami will play in the FIFA Club World Cup next summer...",
    author: "Marca",
    category: "Sports",
    imageUrl: "https://phantom-marca.unidadeditorial.es/7a53057753ff25cc9909bd757bf8ec58/resize/828/f/webp/assets/multimedia/imagenes/2024/10/20/17293869618234.jpg",
    id: 6,
  },
  {
    title: "Messi and Suarez support their sons as mascots in Inter Miami academy match",
    content: "In a captivating display of sportsmanship and family ties, Lionel Messi and Luis Suarez graced the field as mascots for their sons...",
    author: "Marca",
    category: "Sports",
    imageUrl: "https://phantom-marca.unidadeditorial.es/7a53057753ff25cc9909bd757bf8ec58/resize/828/f/webp/assets/multimedia/imagenes/2024/10/20/17293869618234.jpg",
    id: 7,
  },
  {
    title: "Lionel Messi jerseys to test Paraguay's away shirt ban",
    content: "Argentina coach Lionel Scaloni is confident there will be Lionel Messi jerseys in the home section despite the Paraguayan Football Association's (APF) ban...",
    author: "Marca",
    category: "Sports",
    imageUrl: "https://a.espncdn.com/photo/2024/1114/r1414607_1296x518_5-2.jpg",
    id: 8,
  },
  {
    title: "Lionel Messi: Inter Miami will 'come back stronger next year'",
    content: "Lionel Messi vowed to 'come back stronger' in 2025, following Inter Miami's elimination for the 2024 Major League Soccer playoffs...",
    author: "ESPN",
    category: "Sports",
    imageUrl: "https://a.espncdn.com/photo/2024/1111/r1413454_2_1296x518_5-2.jpg",
    id: 9,
  },
  {
    title: "Messi tracker: Inter Miami games, goals, assists, more stats",
    content: "Coming off arguably the biggest sports deal in American history, Lionel Messi's move to Major League Soccer was seismic for the sport's growth...",
    author: "ESPN",
    category: "Sports",
    imageUrl: "https://a.espncdn.com/photo/2024/1110/r1412812_1296x518_5-2.jpg",
    id: 10,
  },
];


const NewsBoard = ({ celeb_name }) => {
  const [articles, setArticles] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        console.log(celeb_name);
        
        // For testing, we're setting the dummy data directly
        const fetchedArticles = dummyData.map(news => ({
          title: news.title,
          description: news.content,
          urlToImage: news.imageUrl,
          url: `https://www.example.com/news/${news.id}`,
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
    <div className="news-board">
      {error ? (
        <p>{error}</p>
      ) : (
        articles.map((article, index) => (
          <div key={index} className="news-item">
            <img src={article.urlToImage} alt={article.title} />
            <h2>{article.title}</h2>
            <p>{article.description}</p>
            <a href={article.url} target="_blank" rel="noopener noreferrer">Read more</a>
          </div>
        ))
      )}
      <Dock />
    </div>
  );
  
};

export default NewsBoard;


