from fastapi import APIRouter, Depends
from Utils.auth.schemas.user_schemas import UserResponse
from Utils.db_dependencies import get_current_user
from Utils.auth.models.models import User


user_router = APIRouter()

@user_router.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username}
