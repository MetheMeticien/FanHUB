from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Utils.auth.routes.auth_route import auth_router
from Features.news.routes.news_route import router as news_router
from Features.social_media.posts.route import router as post_router
from Features.social_media.likes.route import router as like_router
from Features.social_media.comments.route import router as comment_router
from Features.social_media.notifications.route import router as notification_router

from Utils.database import Base,engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(news_router)
app.include_router(post_router)
app.include_router(like_router)
app.include_router(comment_router)
app.include_router(notification_router)


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Auth App"}
