from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from FastAPI.Utils.database import Base, engine
from sqlalchemy.sql import func

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    # Establish relationship with User and Post
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
    
    #optional if user comments an image or video
    media_files = relationship("Media", back_populates="comment", cascade="all, delete")

Comment.metadata.create_all(bind=engine)