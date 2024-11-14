from sqlalchemy.orm import Session
from Features.social_media.likes.model import Like
from Features.social_media.likes.schema import LikeCreate

def create_like(db: Session, like: LikeCreate):
    db_like = Like(**like.dict())
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

def get_likes_by_post(db: Session, post_id: int):
    return db.query(Like).filter(Like.post_id == post_id).all()

def delete_like(db: Session, like_id: int):
    db_like = db.query(Like).filter(Like.id == like_id).first()
    if db_like:
        db.delete(db_like)
        db.commit()
    return db_like
