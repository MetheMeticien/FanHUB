from fastapi import FastAPI
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # Allow frontend running on port 5173
]

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins to allow
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

genai.configure(api_key="AIzaSyDps8o4RTRq4uNZAFFt8e4VlX8niaOxo6A")
model = genai.GenerativeModel("gemini-1.5-flash")



@app.get("/")
def read_root():
    return {"message": "Welcome to the Celebrity Info API"}

@app.get("/celebrity-info/{celebrity_name}")
def get_celebrity_info(celebrity_name: str):
    response = model.generate_content("Introduce this celebrity" + celebrity_name+". Keep it concise, only plain text.")
    return response.text