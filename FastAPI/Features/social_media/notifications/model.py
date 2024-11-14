from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from Utils.database import Base, engine

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    type = Column(String, nullable=False)  
    message = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Integer, default=0)  

    user = relationship("User", back_populates="notifications")
    post = relationship("Post", back_populates="notifications")

Notification.metadata.create_all(bind=engine)
