import requests
from bs4 import BeautifulSoup
from .Scraper import WebScraper
from .Scraper import Story

class SkySportsScraper(WebScraper):
    def __init__(self):
        super().__init__("https://www.skysports.com/")
    
    def extract_all_stories(self):
        self.fetch_homepage()  
        
        soup = BeautifulSoup(self.homepage_content, 'html.parser')
        headlines = soup.find_all('a', class_="sdc-site-tile__headline-link")

        for headline in headlines:
            link = headline.get('href')
            story = self.extract_story(link)
            if(story.headline != "No headline found"):
                self.stories.append(story)
                self.celebrity_find(story)
                # print('*'*20)
                # print(story.headline)
                # print('_'*20)
                # print(story.body) 
                # print('*'*20) 

        
    
    def extract_story(self, link):
        article_url = f"https://www.skysports.com/{link}" 
        response = requests.get(article_url, headers=self.headers)
        article_soup = BeautifulSoup(response.content, 'html.parser')

        headline = article_soup.find('span', class_="sdc-article-header__long-title")
        headline_text = headline.get_text(strip=True) if headline else "No headline found"

        article_body = article_soup.find_all('p')
        body_text = "\n".join([p.get_text(strip=True) for p in article_body]) if article_body else "No article body found"
        
        return Story(headline_text, body_text)
        
        

# ssp = SkySportsScraper()
# ssp.extract_all_stories()
# ssp.printAll()