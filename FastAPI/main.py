from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Utils.auth.routes.auth_route import auth_router
from Features.users.routes.user_route import user_router

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
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Auth App"}
