from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    firstname:str
    lastname:str
    username: str
    password: str
    gender:str

class UserInDB(UserCreate):
    hashed_password: str
    

class UserResponse(BaseModel):
    username: str
    class Config:
        orm_mode = True
        
        
class UserResponse2(BaseModel):
    firstname:str
    lastname:str
    username: str
    gender:str
    class Config:
        orm_mode = True


class FullUserResponse(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    gender: Optional[str]
    bio: Optional[str]
    profile_picture_url: Optional[str]
    created_at: datetime
    is_active: bool
    is_verified: bool



class Token(BaseModel):
    access_token: str
    token_type: str