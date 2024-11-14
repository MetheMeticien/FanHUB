import requests
from bs4 import BeautifulSoup
from .Scraper import WebScraper
from .Scraper import Story

class ESPNScraper(WebScraper):
    def __init__(self):
        super().__init__("https://www.espn.in")
    
    def extract_all_stories(self):
        self.fetch_homepage()  
        
        soup = BeautifulSoup(self.homepage_content, 'html.parser')
        headlines = soup.find_all('a', class_=["contentItem__padding contentItem__padding--border", "contentItem__padding watch-link"])

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
        article_url = f"https://www.espn.in{link}" 
        response = requests.get(article_url, headers=self.headers)
        article_soup = BeautifulSoup(response.content, 'html.parser')

        headline = article_soup.find('h1')
        headline_text = headline.get_text(strip=True) if headline else "No headline found"
        
        article_body = article_soup.find('div', class_='article-body')
        if article_body:
            paragraphs = article_body.find_all('p')
            body_text = "\n".join([p.get_text(strip=True) for p in paragraphs])
        else:
            body_text = "No article body found"
        
        return Story(headline_text, body_text)
        
        

# espn = ESPNScraper()
# espn.extract_all_stories()
# espn.printAll()
