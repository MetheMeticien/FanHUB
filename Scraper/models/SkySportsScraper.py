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
        headlines = soup.find_all('div', class_="sdc-site-tiles__item")

        for item in headlines:
            # Find the headline link within each tile
            headline_link = item.find('a', class_="sdc-site-tile__headline-link")
            if headline_link:
                link = headline_link.get('href')
            else:
                link = "No headline link found"
            
            # Find the image within the nested div structure for the thumbnail
            img_wrap = item.find('div', class_="sdc-site-tile__image-wrap")
            if img_wrap:
                img_tag = img_wrap.find('img', class_="sdc-site-tile__image")
                if img_tag:
                    thumbnail_link = img_tag.get('src', "No image found")
                else:
                    thumbnail_link = "No image found"
            else:
                thumbnail_link = "No image found"
            
            # Now pass both the link and thumbnail link to extract_story
            story = self.extract_story(link, thumbnail_link)

            if(story.headline != "No headline found" and story.body != "No article body found" and story not in self.stories):
                self.stories.append(story)
                self.celebrity_find(story)
                # print('*'*20)
                # print(story.headline)
                # print('_'*20)
                # print(story.body) 
                # print('*'*20) 

        
    
    def extract_story(self, link,thumbnail_link=None):
        try:
            print("Connecting to webpage...")
            article_url = f"https://www.skysports.com/{link}" 
            # Set a timeout of 10 seconds (adjustable as needed)
            response = requests.get(article_url, headers=self.headers, timeout=10)
            print("Connection established")
            
            article_soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract the headline
            headline = article_soup.find('span', class_="sdc-article-header__long-title")
            headline_text = headline.get_text(strip=True) if headline else "No headline found"
            
            # Extract the body content
            article_body = article_soup.find_all('p')
            body_text = "\n".join([p.get_text(strip=True) for p in article_body]) if article_body else "No article body found"
            
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

        return Story(headline_text, body_text,thumbnail_link)        

# ssp = SkySportsScraper()
# ssp.extract_all_stories()
# ssp.printAll()