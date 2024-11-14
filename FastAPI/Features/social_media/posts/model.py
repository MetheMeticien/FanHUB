from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from Utils.database import Base, engine


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(Text, nullable=False)
    published_at = Column(DateTime, default=datetime.utcnow)
    category = Column(String, index=True, nullable=False)
    imageUrl = Column(String, nullable=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))  # Foreign key to User model

    # Establish relationship with User model
    author = relationship("User", back_populates="posts")  # This replaces the old author field
    
    
    notifications = relationship("Notification", back_populates="post")
    likes = relationship("Like", back_populates="post", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")

Post.metadata.create_all(bind=engine)
