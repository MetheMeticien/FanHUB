from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int
    category: str  
    imageUrl: Optional[str] = None

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    user_id: Optional[int] = None
    category: Optional[str] = None  
    imageUrl: Optional[str] = None

class PostOut(PostBase):
    id: int
    published_at: datetime

    class Config:
        orm_mode = True
