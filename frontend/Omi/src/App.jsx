import { useState } from "react"
import Navbar from "./Components/Navbar"
import NewsBoard from "./Components/NewsBoard"
import './App.css';



export const App = () => {
  const [category, setCategory] = useState("entertainment");
  return (
    <div>
        {/* <Navbar setCategory={setCategory}/> */}
        <NewsBoard category={category}/>
    </div>
  )
}


export default App