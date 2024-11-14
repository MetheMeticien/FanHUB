from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from FastAPI.Utils.database import Base, engine
from sqlalchemy.sql import func

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Establish relationship with User and Comments
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete")
    reactions = relationship("Reaction", back_populates="post", cascade="all, delete")
    media_files = relationship("Media", back_populates="post", cascade="all, delete")

Post.metadata.create_all(bind=engine)