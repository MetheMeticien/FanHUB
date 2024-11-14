from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Features.social_media.likes.schema import LikeCreate, LikeOut
import Features.social_media.likes.crud as crud
from Utils.db_dependencies import get_db
from typing import List


router = APIRouter()

@router.post("/likes", response_model=LikeOut)
def create_like(like: LikeCreate, db: Session = Depends(get_db)):
    return crud.create_like(db=db, like=like)

@router.get("/likes/{post_id}", response_model=List[LikeOut])
def get_likes_by_post(post_id: int, db: Session = Depends(get_db)):
    return crud.get_likes_by_post(db=db, post_id=post_id)

@router.delete("/likes/{like_id}", response_model=LikeOut)
def delete_like(like_id: int, db: Session = Depends(get_db)):
    db_like = crud.delete_like(db=db, like_id=like_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like
