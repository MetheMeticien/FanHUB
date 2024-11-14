from pydantic import BaseModel

class LikeBase(BaseModel):
    user_id: int
    post_id: int

class LikeCreate(LikeBase):
    pass

class LikeOut(LikeBase):
    id: int

    class Config:
        orm_mode = True
