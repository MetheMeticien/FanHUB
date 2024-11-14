from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Features.social_media.comments.schema import CommentCreate, CommentOut
import Features.social_media.comments.crud as crud
from Utils.db_dependencies import get_db
from typing import List


router = APIRouter()

@router.post("/comments", response_model=CommentOut)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)

@router.get("/comments/{post_id}", response_model=List[CommentOut])
def get_comments_by_post(post_id: int, db: Session = Depends(get_db)):
    return crud.get_comments_by_post(db=db, post_id=post_id)

@router.delete("/comments/{comment_id}", response_model=CommentOut)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.delete_comment(db=db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment
