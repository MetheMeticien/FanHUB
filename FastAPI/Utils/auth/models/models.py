from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from Utils.database import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    # email = Column(String, unique=True, index=True)
    first_name = Column(String,index=True)
    last_name = Column(String,index=True)
    hashed_password = Column(String)
    gender = Column(String, index=True)
    bio = Column(String, nullable=True)
    profile_picture_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    # posts = relationship("Post", back_populates="author")
    # followers = relationship("Follower", back_populates="user", cascade="all, delete")

User.metadata.create_all(bind=engine)
