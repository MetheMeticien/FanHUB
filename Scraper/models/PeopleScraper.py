import requests
from bs4 import BeautifulSoup
from Scraper import WebScraper
from Scraper import Story

class PeopleScraper(WebScraper):
    def __init__(self):
        super().__init__("https://people.com/celebrity/")
    
    def extract_all_stories(self):
        self.fetch_homepage()  
        
        soup = BeautifulSoup(self.homepage_content, 'html.parser')
        headlines = soup.find_all('a', class_=["card__content "])

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
            article_url = f"https://people.com/celebrity/{link}"
            # Set a timeout of 10 seconds (adjustable as needed)
            response = requests.get(article_url, headers=self.headers, timeout=10)
            print("Connection established")

            article_soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the headline
            headline = article_soup.find('h1')
            headline_text = headline.get_text(strip=True) if headline else "No headline found"

            # Extract the body content
            article_body = article_soup.find('div', class_='loc article-content')
            if article_body:
                paragraphs = article_body.find_all('p')
                body_text = "\n".join([p.get_text(strip=True) for p in paragraphs])

                # Attempt to find an image URL in different potential locations
                img_url = "No image found"
                
                # Check for an image within an <img> tag
                img_tag = article_soup.find('img')
                if img_tag and img_tag.get('src'):
                    img_url = img_tag['src']
                
                # Check for background image in the CSS style attribute
                if img_url == "No image found":
                    img_tag = article_soup.find('div', class_='img-wrap')
                    if img_tag:
                        style_attr = img_tag.get('style', '')
                        if 'background-image' in style_attr:
                            # Extract image URL from background-image style
                            img_url = style_attr.split('url(')[1].split(')')[0].strip('"')
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

        
        

ppl = PeopleScraper()
ppl.extract_all_stories()
ppl.printAll()
