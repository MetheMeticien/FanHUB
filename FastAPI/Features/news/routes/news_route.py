# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from Utils.db_dependencies import get_db
from Features.news.schemas.news_schemas import NewsCreate, NewsOut, NewsUpdate
import Features.news.crud.news_crud as crud

router = APIRouter()

@router.post("/news", response_model=NewsOut)
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    return crud.create_news(db=db, news=news)

@router.get("/news/{news_id}", response_model=NewsOut)
def read_news(news_id: int, db: Session = Depends(get_db)):
    db_news = crud.get_news(db=db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News item not found")
    return db_news

@router.get("/news", response_model=List[NewsOut])
def read_all_news(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_news(db=db, skip=skip, limit=limit)

@router.put("/news/{news_id}", response_model=NewsOut)
def update_news(news_id: int, news: NewsUpdate, db: Session = Depends(get_db)):
    db_news = crud.update_news(db=db, news_id=news_id, news=news)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News item not found")
    return db_news

@router.delete("/news/{news_id}", response_model=NewsOut)
def delete_news(news_id: int, db: Session = Depends(get_db)):
    db_news = crud.delete_news(db=db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News item not found")
    return db_news
