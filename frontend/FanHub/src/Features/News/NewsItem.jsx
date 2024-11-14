const NewsItem = ({title, description, src, url}) => {
  console.log(src);
  return (
    <div className="card bg-dark text-light mb-3 d-inline-block my-3 mx-3 px-2 py-2" style={{maxWidth: "400px", height: "500px"}}>
      <img src={src ? src : image} style={{height: "300px", width: "100%", objectFit: "cover"}} className="card-img-top" alt="..." />
      <div className="card-body d-flex flex-column" style={{height: "200px", paddingBottom: "20px"}}>
        <h5 className="card-title" style={{height: "120px", overflow: "hidden", fontSize: "18px"}}>
          {title !== "[Removed]" ? title : "Breaking News"}
        </h5>
        {/* <p className="card-text" style={{height: "80px", overflow: "hidden", fontSize: "14px"}}>
          {description !== "[Removed]" ? description : "This is placeholder text to fill the space of the description. It ensures consistent layout and design across all cards. It will be fixed later"} 
        </p> */}
        <div className="mt-auto">
          <a href={url} className="btn btn-primary" style={{fontSize: "14px"}}>Read More</a>
        </div>
      </div>
    </div>
  )
}

export default NewsItem
