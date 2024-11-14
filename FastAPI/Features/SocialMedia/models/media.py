from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from FastAPI.Utils.database import Base, engine
from sqlalchemy.sql import func

class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    file_url = Column(String, nullable=False)  
    media_type = Column(Enum(MediaType), nullable=False)  # Type of media
    uploaded_at = Column(DateTime, default=func.now())
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=True)
    comment_id = Column(Integer, ForeignKey("comments.id"), nullable=True)

    # Relationships for Post and Comment
    post = relationship("Post", back_populates="media_files")
    comment = relationship("Comment", back_populates="media_files")

Media.metadata.create_all(bind=engine)