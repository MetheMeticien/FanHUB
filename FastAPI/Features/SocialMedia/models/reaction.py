from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from FastAPI.Utils.database import Base, engine
from sqlalchemy.sql import func

class Reaction(Base):
    __tablename__ = "reactions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)  # e.g., "like", "dislike", etc.
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    # Establish relationship with User and Post
    user = relationship("User", back_populates="reactions")
    post = relationship("Post", back_populates="reactions")


Reaction.metadata.create_all(bind=engine)