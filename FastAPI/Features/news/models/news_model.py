from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
from Utils.database import Base, engine


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(Text, nullable=False)
    author = Column(String, index=True, nullable=False)
    published_at = Column(DateTime, default=datetime.utcnow)
    category = Column(String, index=True, nullable=False) 
    imageUrl = Column(String, nullable=True) 


News.metadata.create_all(bind=engine)