from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from Utils.db_dependencies import get_db
from Features.social_media.posts.schema import PostCreate, PostOut, PostUpdate
import Features.social_media.posts.crud as crud

router = APIRouter()

@router.post("/posts", response_model=PostOut)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@router.get("/posts/{post_id}", response_model=PostOut)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.get("/posts", response_model=List[PostOut])
def read_all_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_posts(db=db, skip=skip, limit=limit)

@router.put("/posts/{post_id}", response_model=PostOut)
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    db_post = crud.update_post(db=db, post_id=post_id, post=post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.delete("/posts/{post_id}", response_model=PostOut)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.delete_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.get("/posts/for_celeb/{celeb_name}", response_model=List[PostOut])
def read_news_by_celeb(celeb_name: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    news = crud.get_posts_by_celeb(db=db, celeb_name=celeb_name, skip=skip, limit=limit)
    if not news:
        raise HTTPException(status_code=404, detail="No news found for this celebrity")
    return news
