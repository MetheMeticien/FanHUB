from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Utils.auth.schemas.user_schemas import UserCreate, UserResponse, Token
from Utils.auth.models.models import User
from Utils.auth.secuirity_functions.hash import hash_password, verify_password
from Utils.auth.secuirity_functions.token import create_access_token
from Utils.db_dependencies import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

auth_router = APIRouter()

@auth_router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
        first_name=user.firstname,
        last_name=user.lastname,
        gender=user.gender
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse(username=db_user.username)

@auth_router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
