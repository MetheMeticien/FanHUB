from fastapi import FastAPI, HTTPException
import httpx
from fastapi.responses import JSONResponse

app = FastAPI()

# Replace with the actual Gemini URL you're using
GEMINI_SERVER_URL = "gemini://localhost:1965/celebrity-info?prompt="

# Function to fetch celebrity data from the Gemini server
async def fetch_gemini_data(celebrity_name: str):
    try:
        # Create an HTTPX client for making asynchronous requests
        async with httpx.AsyncClient() as client:
            # Construct the full URL with the celebrity name
            gemini_url = GEMINI_SERVER_URL + celebrity_name
            # Send a GET request to the Gemini server (this will need to be adapted for Gemini)
            response = await client.get(gemini_url)
            
            # Check if the request was successful
            if response.status_code == 200:
                return response.text  # Gemini responses are usually in plain text
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Gemini server")
    
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from Gemini: {str(e)}")

@app.get("/celebrity-info")
async def get_celebrity_info(celebrity_name: str):
    # Fetch data from Gemini server using the provided celebrity name
    data = await fetch_gemini_data(celebrity_name)
    
    # Return the fetched data as a JSON response
    return JSONResponse(content={"celebrity_info": data})

