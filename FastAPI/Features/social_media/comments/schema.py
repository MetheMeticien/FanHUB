from pydantic import BaseModel
from datetime import datetime

class CommentBase(BaseModel):
    post_id: int
    user_id: int
    content: str

class CommentCreate(CommentBase):
    pass

class CommentOut(CommentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
