import React, { useEffect, useState } from 'react';
import '../Celeb/css/Banner.css';

const Banner = ({ image, name }) => {
  const [description, setDescription] = useState('');

  // Fetch description from FastAPI server using celebrity name
  useEffect(() => {
    const fetchDescription = async () => {
      try {
        const response = await fetch(`http://localhost:8001/celebrity-info/${name}`);
        if (response.ok) {
          const data = await response.text();
          const cleanData = data.replace(/[\r\n]+/g, ' ').replace(/["]+/g, '').trim();


          console.log(cleanData)
          setDescription(cleanData); // Assuming the API returns { message: 'description' }
        } else {
          setDescription('Description not available.');
        }
      } catch (error) {
        setDescription('Error fetching description.');
      }
    };

    fetchDescription();
  }, [name]); // Re-fetch if the name changes

  return (
    <div className="banner-container">
      <img src={image} alt="Banner" className="banner-image" />
      <div className="banner-content">
        <h1 className="banner-title">{name}</h1>
        <p className="banner-description">{description}</p>
      </div>
    </div>
  );
};

export default Banner;
