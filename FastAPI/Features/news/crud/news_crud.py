# crud.py
from sqlalchemy.orm import Session
from Features.news.models.news_model import News
from Features.news.schemas.news_schemas import NewsCreate, NewsUpdate

def create_news(db: Session, news: NewsCreate):
    print(f"Creating news with data: {news.dict()}") 
    db_news = News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

# async def create_news_from_story(news_data: NewsCreate, db: Session):
#     return await create_news(news=news_data, db=db)

def get_news(db: Session, news_id: int):
    return db.query(News).filter(News.id == news_id).first()

def get_all_news(db: Session, skip: int = 0, limit: int = 10):
    return db.query(News).offset(skip).limit(limit).all()

def get_news_by_celeb(db: Session, celeb_name: str, skip: int = 0, limit: int = 10):
    return db.query(News).filter(News.celeb_tags.like(f"%{celeb_name}%")).offset(skip).limit(limit).all()


def update_news(db: Session, news_id: int, news: NewsUpdate):
    db_news = get_news(db, news_id)
    if db_news:
        for key, value in news.dict(exclude_unset=True).items():
            setattr(db_news, key, value)
        db.commit()
        db.refresh(db_news)
    return db_news

def delete_news(db: Session, news_id: int):
    db_news = get_news(db, news_id)
    if db_news:
        db.delete(db_news)
        db.commit()
    return db_news
