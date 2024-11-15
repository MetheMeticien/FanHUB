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
        try:
            print("Connecting to webpage...")
            article_url = f"https://www.espn.in{link}"
            # Set a timeout of 10 seconds (adjustable as needed)
            response = requests.get(article_url, headers=self.headers, timeout=10)
            print("Connection established")

            article_soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the headline
            headline = article_soup.find('h1')
            headline_text = headline.get_text(strip=True) if headline else "No headline found"

            # Extract the body content
            article_body = article_soup.find('div', class_='article-body')
            if article_body:
                paragraphs = article_body.find_all('p')
                body_text = "\n".join([p.get_text(strip=True) for p in paragraphs])
                
                img_wrap = article_soup.find('div', class_='img-wrap')
                if img_wrap:
                    source_tag = img_wrap.find('source')  # Look for the first source tag within img-wrap
                    img_url = source_tag['srcset'].split(',')[0].strip() if source_tag and 'srcset' in source_tag.attrs else "No image found"
                else:
                    img_url = "No image found"

            else:
                body_text = "No article body found"
                img_url = "No image found"

        except requests.exceptions.Timeout:
            print("Connection timed out")
            # Return a story with a placeholder headline and body text
            headline_text = "No headline found"
            body_text = "Connection timed out"

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            # Return a story with a placeholder headline and body text for any other request errors
            headline_text = "No headline found"
            body_text = str(e)

        return Story(headline_text, body_text,img_url)

        
        

# espn = ESPNScraper()
# espn.extract_all_stories()
# espn.printAll()
