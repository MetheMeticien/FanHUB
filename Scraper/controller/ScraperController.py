import sys
import os
import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import *  

class ScraperController:
    def __init__(self):
        self.scrapers = [scraper_class() for scraper_class in WebScraper.__subclasses__()]

    def scrape_all(self):
        for scraper in self.scrapers:
            scraper.extract_all_stories()
            scraper.printAll()
    
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
# print("Finding Story on Lebron James")
# sc.scrape_celeb_with_date("LeBron James", date=datetime.date.today())
# print("Finding Stories from today!")
# sc.scrape_with_date(datetime.date.today())

sc.scrape_all()