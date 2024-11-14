from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Utils.database import Base, engine


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    post = relationship("Post", back_populates="likes")
    user = relationship("User", back_populates="likes")

    def __repr__(self):
        return f"<Like(post_id={self.post_id}, user_id={self.user_id})>"

Like.metadata.create_all(bind=engine)