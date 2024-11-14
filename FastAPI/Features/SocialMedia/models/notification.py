from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from FastAPI.Utils.database import Base, engine
from sqlalchemy.sql import func

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    is_read = Column(Boolean, default=False)

    # Relationship with User
    user = relationship("User", backref="notifications")

Notification.metadata.create_all(bind=engine)
