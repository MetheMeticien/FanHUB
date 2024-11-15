import { Routes, Route, useParams } from "react-router-dom";
import NewsBoard from "../News/NewsBoard";
import PostPage from "../PostPage/PostPage";
import Banner from "./Banner";

const CelebPage = () => {
  const { celeb_name } = useParams(); // Access dynamic param
  const sampleImage = "https://s.france24.com/media/display/451ed2b8-eed6-11ea-afdd-005056bf87d6/w:980/p:16x9/messi-1805.jpg"; // Replace with an actual image URL

  return (
    <div>
      <Banner image={sampleImage} name={celeb_name} />
      
      <Routes>
        <Route path="news" element={<NewsBoard celeb_name={celeb_name}/>} />
        <Route path="posts" element={<PostPage />} />
      </Routes>
    </div>
  );
};

export default CelebPage;
