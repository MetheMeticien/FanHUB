import sys
import os
import datetime
import httpx
import asyncio
import Features.news.crud.news_crud as crud
from Utils.db_dependencies import get_db
from Features.news.schemas.news_schemas import NewsCreate
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import *  



class ScraperController:
    def __init__(self):
        self.api_url = "http://localhost:8000"
        self.scrapers = [scraper_class() for scraper_class in WebScraper.__subclasses__()]

    async def scrape_all(self, db: Session):  # Ensure db is passed as a parameter
        for scraper in self.scrapers:
            scraper.extract_all_stories()  # Assuming this method scrapes the stories
            # scraper.printAll()  # Assuming this prints the stories

            for story in scraper.stories:
                # Convert each story to NewsCreate schema
                news_create = story.to_news_create(
                    
                    author="John Doe", 
                    category="Movies", 
                    imageUrl="http://image.url"
                )
                
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        f"{self.api_url}/news", json=news_create.dict()
                    )

                # Check if the request was successful
                if response.status_code == 200:
                    print(f"Successfully created news: {news_create.title}")
                else:
                    print(f"Failed to create news: {news_create.title}, Error: {response.text}")
                
    
    def scrape_celeb_with_date(self, celeb_name, date):
        for scraper in self.scrapers:
            scraper.extract_all_stories()
            for story in scraper.stories:
                if celeb_name in story.celeb_tags and story.date_time == date:
                    story.printStory()
    
    def scrape_with_date(self, date):
        for scraper in self.scrapers:
            print("New Scraper Initiated!")
            scraper.extract_all_stories()
            for story in scraper.stories:
                print("Checking New Story!")
                if story.date_time == date:
                    story.printStory()


sc = ScraperController()

# Define an async function to call scrape_all
async def run_scraper():
    db = get_db()  # You can get the database session here
    await sc.scrape_all(db=db)  # Call the async method

# Run the scraper using asyncio
if __name__ == "__main__":
    asyncio.run(run_scraper())