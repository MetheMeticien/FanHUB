from fastapi import FastAPI, HTTPException
import httpx
from fastapi.responses import JSONResponse

app = FastAPI()

GEMINI_SERVER_URL = "gemini://localhost:1965/celebrity-info?prompt="

async def fetch_gemini_data(celebrity_name: str):
    try:
        async with httpx.AsyncClient() as client:
            gemini_url = GEMINI_SERVER_URL + celebrity_name
            response = await client.get(gemini_url)

            if response.status_code == 200:
                return response.text 
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Gemini server")
    
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from Gemini: {str(e)}")

@app.get("/celebrity-info")
async def get_celebrity_info(celebrity_name: str):

    data = await fetch_gemini_data(celebrity_name)
    return JSONResponse(content={"celebrity_info": data})

