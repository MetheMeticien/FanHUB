import requests
from bs4 import BeautifulSoup
from .Scraper import WebScraper
from .Scraper import Story

class DailyMailScraper(WebScraper):
    def __init__(self):
        super().__init__("https://www.dailymail.co.uk/tvshowbiz/index.html")
    
    def extract_all_stories(self):
        self.fetch_homepage()  
        
        soup = BeautifulSoup(self.homepage_content, 'html.parser')
        headlines = soup.find_all('a', itemprop="url")

        for headline in headlines:
            link = headline.get('href')
            if link:
                link = link.replace("index.html", "")
                full_link = f"https://www.dailymail.co.uk{link}"
                story = self.extract_story(full_link)
                if story.headline != "No headline found":
                    self.stories.append(story)
                    self.celebrity_find(story)
                    # print('*'*20)
                    # print(story.headline)
                    # print('_'*20)
                    # print(story.body) 
                    # print('*'*20)  

    
    def extract_story(self, link):
        response = requests.get(link, headers=self.headers)
        article_soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting the headline from the first <h1>
        headline = article_soup.find('h1')
        headline_text = headline.get_text(strip=True) if headline else "No headline found"
        
        # Extracting the body content from all <p> tags
        paragraphs = article_soup.find_all('p')
        if paragraphs:
            body_text = "\n".join([p.get_text(strip=True) for p in paragraphs])
        else:
            body_text = "No article body found"
        
        return Story(headline_text, body_text)



# dailymail = DailyMailScraper()
# dailymail.extract_all_stories()
# dailymail.printAll()
