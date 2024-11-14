from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsBase(BaseModel):
    title: str
    content: str
    author: str
    category: str  
    imageUrl: Optional[str] = None
    celeb_tags: Optional[str] = None

class NewsCreate(NewsBase):
    pass

class NewsUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None  
    imageUrl: Optional[str] = None
    celeb_tags: Optional[str] = None

class NewsOut(NewsBase):
    id: int
    published_at: datetime

    class Config:
        orm_mode = True
