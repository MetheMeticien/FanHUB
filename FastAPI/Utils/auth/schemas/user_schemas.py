from pydantic import BaseModel

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

class Token(BaseModel):
    access_token: str
    token_type: str