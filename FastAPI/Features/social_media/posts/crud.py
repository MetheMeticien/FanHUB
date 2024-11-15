from sqlalchemy.orm import Session
from Features.social_media.posts.model import Post
from Features.social_media.posts.schema import PostCreate, PostUpdate
from Utils.auth.models.models import User


def create_post(db: Session, post: PostCreate):

    user_instance = db.query(User).filter(User.id == post.user_id).first()
    
    if not user_instance:
        raise ValueError("User not found")


    db_post = Post(
        title=post.title,
        content=post.content,
        category=post.category,
        imageUrl=post.imageUrl,
        user_id=post.user_id,  
        author=user_instance,
        celeb_tags = post.celeb_tags
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_all_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def get_posts_by_celeb(db: Session, celeb_name: str, skip: int = 0, limit: int = 10):
    return db.query(Post).filter(Post.celeb_tags.like(f"%{celeb_name}%")).offset(skip).limit(limit).all()

def update_post(db: Session, post_id: int, post: PostUpdate):
    db_post = get_post(db, post_id)
    if db_post:
        for key, value in post.dict(exclude_unset=True).items():
            setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = get_post(db, post_id)
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post
